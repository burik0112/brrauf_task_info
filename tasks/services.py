import aiohttp
import asyncio
import logging
import time
from django.conf import settings

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = aiohttp.ClientTimeout(total=15)
MAX_PAGES = 20
CACHE_TTL = 600


class BitrixService:
    def __init__(self):
        self.base_url = settings.BITRIX_WEBHOOK_URL.rstrip('/')
        self._session = None
        self._users_cache = None
        self._cache_timestamp = 0.0

    async def _get_session(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(timeout=REQUEST_TIMEOUT)
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None

    async def get_user(self, bitrix_id):
        try:
            session = await self._get_session()
            async with session.get(
                f"{self.base_url}/user.get",
                params={"ID": bitrix_id},
            ) as resp:
                data = await resp.json()
                users = data.get("result", [])
                if users:
                    user = users[0]
                    return {
                        "id": int(user["ID"]),
                        "name": user.get("NAME", ""),
                        "last_name": user.get("LAST_NAME", ""),
                        "full_name": f"{user.get('NAME', '')} {user.get('LAST_NAME', '')}".strip(),
                        "personal_phone": user.get("PERSONAL_PHONE", ""),
                        "personal_mobile": user.get("PERSONAL_MOBILE", ""),
                    }
                return None
        except asyncio.TimeoutError:
            logger.warning(f"Bitrix get_user timeout: {bitrix_id}")
            return None
        except Exception:
            logger.exception(f"Bitrix get_user error: {bitrix_id}")
            return None

    async def create_task(self, title, creator_id, responsible_id, description=""):
        try:
            session = await self._get_session()
            async with session.post(
                f"{self.base_url}/tasks.task.add",
                json={
                    "fields": {
                        "TITLE": title,
                        "DESCRIPTION": description,
                        "CREATED_BY": creator_id,
                        "RESPONSIBLE_ID": responsible_id,
                    }
                },
            ) as resp:
                data = await resp.json()
                logger.info(f"Bitrix create_task response: {data}")
                error = data.get("error")
                if error:
                    error_description = data.get("error_description", error)
                    return {"ok": False, "error": error_description}
                result = data.get("result", {})
                task = result.get("task", {})
                if task:
                    return {"ok": True, "id": task.get("id"), "title": task.get("title"), "link": task.get("link", "")}
                return {"ok": False, "error": "Bitrix javobida topilmadi"}
        except asyncio.TimeoutError:
            logger.warning(f"Bitrix create_task timeout: {title}")
            return {"ok": False, "error": "Bitrix24 javob bermadi (timeout)"}
        except Exception as exc:
            logger.exception(f"Bitrix create_task error: {title}")
            return {"ok": False, "error": str(exc)}

    async def _fetch_all_users_uncached(self):
        all_users = []
        start = 0
        session = await self._get_session()
        for _ in range(MAX_PAGES):
            async with session.get(
                f"{self.base_url}/user.get",
                params={"start": start},
            ) as resp:
                data = await resp.json()
                users = data.get("result", [])
                for u in users:
                    all_users.append({
                        "id": int(u["ID"]),
                        "name": u.get("NAME", ""),
                        "last_name": u.get("LAST_NAME", ""),
                        "full_name": f"{u.get('NAME', '')} {u.get('LAST_NAME', '')}".strip(),
                    })
                next_start = data.get("next")
                if next_start and int(next_start) > start:
                    start = int(next_start)
                else:
                    break
        return all_users

    async def get_all_users(self):
        try:
            now = time.monotonic()
            if self._users_cache is not None and (now - self._cache_timestamp) < CACHE_TTL:
                return self._users_cache

            all_users = await self._fetch_all_users_uncached()
            if all_users:
                self._users_cache = all_users
                self._cache_timestamp = now
            return all_users
        except asyncio.TimeoutError:
            logger.warning("Bitrix get_all_users timeout")
            return self._users_cache or []
        except Exception:
            logger.exception("Bitrix get_all_users error")
            return self._users_cache or []

    async def get_top_users(self, recent_ids, limit=10):
        all_users = await self.get_all_users()
        if not all_users:
            return []

        recent_set = set(recent_ids)
        recent_users = [u for u in all_users if u["id"] in recent_set]
        other_users = [u for u in all_users if u["id"] not in recent_set]

        ordered = recent_users + other_users
        return ordered[:limit]

    async def search_users(self, query, limit=10):
        all_users = await self.get_all_users()
        if not all_users:
            return []

        query_lower = query.lower()
        matched = [
            u for u in all_users
            if query_lower in u["full_name"].lower()
        ]
        return matched[:limit]

    async def attach_file_to_task(self, task_id, file_name, file_content):
        try:
            import base64
            content_b64 = base64.b64encode(file_content).decode("utf-8")
            session = await self._get_session()
            async with session.post(
                f"{self.base_url}/task.item.addfile",
                json={
                    "TASK_ID": str(task_id),
                    "FILE": {
                        "NAME": file_name,
                        "CONTENT": content_b64,
                    }
                },
            ) as resp:
                data = await resp.json()
                logger.info(f"Bitrix attach_file response: {data}")
                return "result" in data
        except asyncio.TimeoutError:
            logger.warning(f"Bitrix attach_file timeout: task={task_id}, file={file_name}")
            return False
        except Exception:
            logger.exception(f"Bitrix attach_file error: task={task_id}, file={file_name}")
            return False


bitrix_service = BitrixService()
