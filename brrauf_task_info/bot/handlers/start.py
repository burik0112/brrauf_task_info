import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from asgiref.sync import sync_to_async

from bot.keyboards.main_menu import get_main_menu
from bot.states.registration import RegistrationState
from users.models import TelegramUser

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    try:
        user, _created = await sync_to_async(TelegramUser.objects.get_or_create)(
            telegram_id=message.from_user.id,
            defaults={
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
            }
        )

        if user.is_registered:
            await message.answer(
                f"Assalomu alaykum, {user.first_name or user.username}! 👋\n\n"
                "Xush kelibsiz! Quyidagi menyudan foydalaning:",
                reply_markup=get_main_menu(),
            )
            await state.clear()
        else:
            await message.answer(
                "Xush kelibsiz! Ro'yxatdan o'tish uchun Bitrix ID kiriting:\n\n"
                "Bitrix ID ni https://brrauf.bitrix24.uz dan olishingiz mumkin.",
            )
            await state.set_state(RegistrationState.waiting_for_bitrix_id)
    except Exception:
        logger.exception('Error in /start handler')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")
