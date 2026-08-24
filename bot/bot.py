import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from bot.handlers.registration import router as registration_router
from bot.handlers.start import router as start_router
from bot.handlers.tasks import router as tasks_router
from tasks.services import bitrix_service

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_storage():
    redis_url = os.getenv('REDIS_URL')
    if redis_url:
        try:
            from aiogram.fsm.storage.redis import RedisStorage
            logger.info('Using RedisStorage')
            return RedisStorage.from_url(redis_url)
        except ImportError:
            logger.warning('redis not installed, falling back to MemoryStorage')
        except Exception:
            logger.warning('RedisStorage failed, falling back to MemoryStorage')
    logger.info('Using MemoryStorage (state will be lost on restart)')
    return MemoryStorage()


async def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error('TELEGRAM_BOT_TOKEN is not set in .env file!')
        return

    from django.conf import settings as django_settings
    if not django_settings.BITRIX_WEBHOOK_URL:
        logger.error(
            'BITRIX_WEBHOOK_URL is not set. Bot cannot start without Bitrix24 connection. '
            'Set BITRIX_WEBHOOK_URL in .env file.'
        )
        return

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=get_storage())

    dp.include_router(start_router)
    dp.include_router(registration_router)
    dp.include_router(tasks_router)

    logger.info('Bot is starting...')
    try:
        await dp.start_polling(bot, drop_pending_updates=True)
    finally:
        await bitrix_service.close()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
