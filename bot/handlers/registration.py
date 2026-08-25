import html
import logging

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from asgiref.sync import sync_to_async

from bot.keyboards.main_menu import get_main_menu
from bot.states.registration import RegistrationState
from tasks.services import bitrix_service
from users.models import TelegramUser

router = Router()
logger = logging.getLogger(__name__)


@router.message(RegistrationState.waiting_for_bitrix_id, F.text)
async def process_bitrix_id(message: Message, state: FSMContext):
    try:
        text = message.text.strip()
        if not text.isdigit():
            await message.answer("Iltimos, faqat raqam kiriting. Masalan: 29")
            return

        bitrix_id = int(text)

        existing_user = await sync_to_async(
            lambda: TelegramUser.objects.filter(bitrix_id=bitrix_id).exclude(
                telegram_id=message.from_user.id
            ).first()
        )()
        if existing_user:
            await message.answer(
                "❌ Bu Bitrix ID allaqachon boshqa akkauntga bog'langan.\n\n"
                "Agar bu sizning ID'ingiz bo'lsa, administrator bilan bog'laning."
            )
            return

        await message.answer("⏳ Bitrix24 dan ma'lumot olinmoqda...")

        user_data = await bitrix_service.get_user(bitrix_id)
        if not user_data:
            await message.answer(
                "❌ Bitrix24 da foydalanuvchi topilmadi.\n\n"
                "Iltimos, to'g'ri Bitrix ID kiriting yoki /start ni bosing."
            )
            return

        full_name = user_data['full_name']
        bitrix_first_name = user_data['name']
        bitrix_last_name = user_data['last_name']

        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id
        )
        user.first_name = message.from_user.first_name or bitrix_first_name
        user.last_name = message.from_user.last_name or bitrix_last_name
        user.bitrix_id = bitrix_id
        user.bitrix_first_name = bitrix_first_name
        user.bitrix_last_name = bitrix_last_name
        user.is_registered = True
        await sync_to_async(user.save)()

        await message.answer(
            f"Ro'yxatdan o'tish tugallandi! ✅\n\n"
            f"Xush kelibsiz, {html.escape(full_name)}!\n\n"
            "Quyidagi menyudan foydalaning:",
            reply_markup=get_main_menu(),
        )
        await state.clear()
    except TelegramUser.DoesNotExist:
        logger.error('User not found during registration')
        await message.answer("Xatolik: Foydalanuvchi topilmadi. /start buyrug'ini bosing.")
        await state.clear()
    except Exception:
        logger.exception('Error in process_bitrix_id')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")


@router.message(RegistrationState.waiting_for_bitrix_id)
async def process_bitrix_id_invalid(message: Message, state: FSMContext):
    await message.answer("Iltimos, Bitrix ID raqamini kiriting. Masalan: 29")
