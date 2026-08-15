from aiogram import Router, F
from aiogram.types import Message, Contact, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async
import logging

from users.models import TelegramUser
from bot.states.registration import RegistrationState
from bot.keyboards.main_menu import get_main_menu

router = Router()
logger = logging.getLogger(__name__)


@router.message(RegistrationState.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    try:
        name = message.text.strip()
        if not name or len(name) < 2:
            await message.answer("Ismingiz juda qisqa. Iltimos, to'liq ismingizni kiriting:")
            return

        await state.update_data(first_name=name)

        phone_keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='📱 Telefon raqamni ulashish', request_contact=True)]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

        await message.answer(
            "Endi telefon raqamingizni ulashing. 📱\n"
            "Quyidagi tugmani bosing:",
            reply_markup=phone_keyboard,
        )
        await state.set_state(RegistrationState.waiting_for_phone)
    except Exception as e:
        logger.exception('Error in process_name')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")


@router.message(RegistrationState.waiting_for_phone, F.contact)
async def process_phone(message: Message, state: FSMContext):
    try:
        contact = message.contact
        phone_number = contact.phone_number

        data = await state.get_data()
        first_name = data.get('first_name', message.from_user.first_name)

        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id
        )
        user.first_name = first_name
        user.phone_number = phone_number
        user.is_registered = True
        await sync_to_async(user.save)()

        await message.answer(
            f"Ro'yxatdan o'tish tugallandi! ✅\n\n"
            f"Xush kelibsiz, {first_name}!\n\n"
            "Quyidagi menyudan foydalaning:",
            reply_markup=get_main_menu(),
        )
        await state.clear()
    except TelegramUser.DoesNotExist:
        logger.error('User not found during registration')
        await message.answer("Xatolik: Foydalanuvchi topilmadi. /start buyrug'ini bosing.")
        await state.clear()
    except Exception as e:
        logger.exception('Error in process_phone')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")
        await state.clear()


@router.message(RegistrationState.waiting_for_phone)
async def process_phone_invalid(message: Message, state: FSMContext):
    await message.answer(
        "Iltimos, telefon raqamini ulashish uchun quyidagi tugmani bosing. 📱"
    )
