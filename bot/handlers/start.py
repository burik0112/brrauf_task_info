from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async
from django.conf import settings
import html
import logging

from users.models import TelegramUser
from bot.states.registration import RegistrationState
from bot.keyboards.main_menu import get_main_menu

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    try:
        user, created = await sync_to_async(TelegramUser.objects.get_or_create)(
            telegram_id=message.from_user.id,
            defaults={
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
            }
        )

        if not created:
            updated = False
            if user.username != message.from_user.username:
                user.username = message.from_user.username
                updated = True
            if user.first_name != message.from_user.first_name:
                user.first_name = message.from_user.first_name
                updated = True
            if user.last_name != message.from_user.last_name:
                user.last_name = message.from_user.last_name
                updated = True
            if updated:
                await sync_to_async(user.save)()

        if user.is_registered:
            display_name = html.escape(user.first_name or user.username or '')
            await message.answer(
                f"Assalomu alaykum, {display_name}! 👋\n\n"
                "Xush kelibsiz! Quyidagi menyudan foydalaning:",
                reply_markup=get_main_menu(),
            )
            await state.clear()
        else:
            await message.answer(
                "Xush kelibsiz! Ro'yxatdan o'tish uchun Bitrix ID kiriting:\n\n"
                f"Bitrix ID ni {settings.BITRIX_PORTAL_URL or 'Bitrix24 portalidan'} dan olishingiz mumkin.",
            )
            await state.set_state(RegistrationState.waiting_for_bitrix_id)
    except Exception:
        logger.exception('Error in /start handler')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")


@router.message(Command('cancel'))
async def cmd_cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Bekor qilish uchun hech narsa yo'q.")
        return
    await state.clear()
    await message.answer(
        "Amal bekor qilindi.",
        reply_markup=get_main_menu(),
    )


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        "🤖 <b>Yordam</b>\n\n"
        "Buyruqlar:\n"
        "/start — Botni qayta ishga tushirish\n"
        "/cancel — Joriy amalni bekor qilish\n"
        "/help — Shu yordam\n\n"
        "Vazifa yaratish uchun asosiy menyudan "
        "<b>📋 Vazifa yaratish</b> tugmasini bosing.",
        parse_mode='HTML',
    )
