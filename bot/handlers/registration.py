import html
import logging
import re

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
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
        bitrix_phone = user_data.get('personal_phone', '') or user_data.get('personal_mobile', '')
        if not bitrix_phone:
            bitrix_phone = ''

        await state.update_data(
            bitrix_id=bitrix_id,
            bitrix_first_name=user_data['name'],
            bitrix_last_name=user_data['last_name'],
            bitrix_phone=bitrix_phone,
        )

        phone_keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='📱 Telefon raqamni ulashish', request_contact=True)]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

        await message.answer(
            f"✅ Topildi: <b>{html.escape(full_name)}</b>\n\n"
            "Telefon raqamingizni ulashing 📱\n"
            "Quyidagi tugmani bosing:",
            parse_mode='HTML',
            reply_markup=phone_keyboard,
        )
        await state.set_state(RegistrationState.waiting_for_phone)
    except Exception:
        logger.exception('Error in process_bitrix_id')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")


@router.message(RegistrationState.waiting_for_bitrix_id)
async def process_bitrix_id_invalid(message: Message, state: FSMContext):
    await message.answer("Iltimos, Bitrix ID raqamini kiriting. Masalan: 29")


@router.message(RegistrationState.waiting_for_phone, F.contact)
async def process_phone(message: Message, state: FSMContext):
    try:
        contact = message.contact

        if contact.user_id != message.from_user.id:
            await message.answer(
                "❌ Iltimos, faqat o'zingizning telefon raqamingizni ulang.\n"
                "Boshqa odamning kontakt kartasini yubormang."
            )
            return

        phone_number = contact.phone_number

        data = await state.get_data()
        bitrix_id = data.get('bitrix_id')
        bitrix_first_name = data.get('bitrix_first_name', '')
        bitrix_last_name = data.get('bitrix_last_name', '')
        bitrix_phone = data.get('bitrix_phone', '')
        full_name = f"{bitrix_first_name} {bitrix_last_name}".strip()

        if not bitrix_phone:
            logger.warning(
                'Phone verification skipped: bitrix phone is empty',
                extra={'telegram_id': message.from_user.id, 'bitrix_id': bitrix_id},
            )
            await message.answer(
                "❌ Bitrix24 profilingizda telefon raqami ko'rsatilmagan.\n\n"
                "Administratorga murojaat qiling yoki /start ni bosing.",
            )
            return

        def extract_digits(phone: str) -> str:
            return re.sub(r'\D', '', phone)

        bitrix_digits = extract_digits(bitrix_phone)
        contact_digits = extract_digits(phone_number)

        if not bitrix_digits or not contact_digits:
            logger.warning(
                'Phone verification failed: empty digits after normalization',
                extra={'telegram_id': message.from_user.id, 'bitrix_id': bitrix_id},
            )
            await message.answer(
                f"❌ Ulashgan raqamingiz Bitrix24 dagi raqamingizga mos kelmaydi.\n\n"
                f"Bitrix24 dagi raqamingiz: <code>{html.escape(bitrix_phone)}</code>\n\n"
                "Iltimos, to'g'ri raqamni ulang yoki /start ni bosing.",
                parse_mode='HTML',
            )
            return

        bitrix_last9 = bitrix_digits[-9:]
        contact_last9 = contact_digits[-9:]

        if bitrix_last9 != contact_last9:
            logger.warning(
                'Phone verification failed: last 9 digits do not match',
                extra={
                    'telegram_id': message.from_user.id,
                    'bitrix_id': bitrix_id,
                    'bitrix_last9': bitrix_last9,
                    'contact_last9': contact_last9,
                },
            )
            await message.answer(
                f"❌ Ulashgan raqamingiz Bitrix24 dagi raqamingizga mos kelmaydi.\n\n"
                f"Bitrix24 dagi raqamingiz: <code>{html.escape(bitrix_phone)}</code>\n\n"
                "Iltimos, to'g'ri raqamni ulang yoki /start ni bosing.",
                parse_mode='HTML',
            )
            return

        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id
        )
        user.first_name = message.from_user.first_name or bitrix_first_name
        user.last_name = message.from_user.last_name or bitrix_last_name
        user.phone_number = phone_number
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
        logger.exception('Error in process_phone')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")
        await state.clear()


@router.message(RegistrationState.waiting_for_phone)
async def process_phone_invalid(message: Message, state: FSMContext):
    await message.answer(
        "Iltimos, telefon raqamini ulashish uchun quyidagi tugmani bosing. 📱"
    )
