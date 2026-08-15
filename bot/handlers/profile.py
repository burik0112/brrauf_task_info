from aiogram import Router, F
from aiogram.types import Message
from asgiref.sync import sync_to_async
import logging

from users.models import TelegramUser
from bot.keyboards.main_menu import get_main_menu

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.text == '👤 Profil')
async def profile(message: Message):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id, is_registered=True
        )
        task_count = await sync_to_async(user.tasks.count)()

        profile_text = (
            f"👤 <b>Profil</b>\n\n"
            f"📝 <b>Ism:</b> {user.first_name or 'Kiritilmagan'}\n\n"
            f"👤 <b>Username:</b> @{user.username or 'Yoq'}\n\n"
            f"📱 <b>Telefon:</b> {user.phone_number or 'Kiritilmagan'}\n\n"
            f"🆔 <b>Telegram ID:</b> {user.telegram_id}\n\n"
            f"📅 <b>Ro'yxatdan o'tgan sana:</b>\n{user.created_at.strftime('%d.%m.%Y %H:%M')}\n\n"
            f"📊 <b>Vazifalar soni:</b> {task_count}"
        )

        await message.answer(profile_text, parse_mode='HTML', reply_markup=get_main_menu())
    except TelegramUser.DoesNotExist:
        await message.answer(
            "Siz hali ro'yxatdan o'tmaganishingiz.\n"
            "Ro'yxatdan o'tish uchun /start buyrug'ini bosing.",
            reply_markup=get_main_menu(),
        )
    except Exception as e:
        logger.exception('Error in profile')
        await message.answer("Xatolik yuz berdi. Qaytadan urinib ko'ring.")
