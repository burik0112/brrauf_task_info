import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from bot.handlers.start import router as start_router
from bot.handlers.registration import router as registration_router
from bot.handlers.tasks import router as tasks_router
from bot.handlers.task_list import router as task_list_router
from bot.handlers.profile import router as profile_router
from bot.handlers.help import router as help_router

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error('TELEGRAM_BOT_TOKEN is not set in .env file!')
        return

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(registration_router)
    dp.include_router(tasks_router)
    dp.include_router(task_list_router)
    dp.include_router(profile_router)
    dp.include_router(help_router)

    logger.info('Bot is starting...')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
