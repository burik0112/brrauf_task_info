import aiohttp
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class BitrixService:
    def __init__(self):
        self.base_url = settings.BITRIX_WEBHOOK_URL.rstrip('/')

    async def get_user(self, bitrix_id: int) -> dict | None:
        try:
            async with aiohttp.ClientSession() as session:
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
                        }
                    return None
        except Exception as e:
            logger.exception(f"Bitrix get_user error: {bitrix_id}")
            return None

    async def create_task(self, title: str, creator_id: int, responsible_id: int, description: str = '') -> dict | None:
        try:
            async with aiohttp.ClientSession() as session:
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
                    result = data.get("result", {})
                    task = result.get("task", {})
                    if task:
                        return {"id": task.get("id"), "title": task.get("title"), "link": task.get("link", "")}
                    return None
        except Exception as e:
            logger.exception(f"Bitrix create_task error: {title}")
            return None

    async def get_all_users(self) -> list[dict]:
        try:
            all_users = []
            start = 0
            async with aiohttp.ClientSession() as session:
                while True:
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
        except Exception as e:
            logger.exception("Bitrix get_all_users error")
            return []

    async def get_top_users(self, recent_ids: list[int], limit: int = 10) -> list[dict]:
        all_users = await self.get_all_users()
        if not all_users:
            return []

        recent_set = set(recent_ids)
        recent_users = [u for u in all_users if u['id'] in recent_set]
        other_users = [u for u in all_users if u['id'] not in recent_set]

        ordered = recent_users + other_users
        return ordered[:limit]

    async def search_users(self, query: str, limit: int = 10) -> list[dict]:
        all_users = await self.get_all_users()
        if not all_users:
            return []

        query_lower = query.lower()
        matched = [
            u for u in all_users
            if query_lower in u['full_name'].lower()
        ]
        return matched[:limit]

    async def attach_file_to_task(self, task_id: int, file_name: str, file_content: bytes) -> bool:
        try:
            import base64
            content_b64 = base64.b64encode(file_content).decode('utf-8')
            async with aiohttp.ClientSession() as session:
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
        except Exception as e:
            logger.exception(f"Bitrix attach_file error: task={task_id}, file={file_name}")
            return False


bitrix_service = BitrixService()
