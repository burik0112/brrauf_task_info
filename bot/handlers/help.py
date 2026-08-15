from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.main_menu import get_main_menu

router = Router()


@router.message(F.text == 'ℹ️ Yordam')
async def help_command(message: Message):
    help_text = (
        "ℹ️ <b>Yordam</b>\n\n"
        "Bu bot vazifalarni boshqarish uchun mo'ljallangan.\n\n"
        "📋 <b>Vazifa yaratish:</b>\n"
        "1. \"📋 Vazifa yaratish\" tugmasini bosing\n"
        "2. Vazifani matn ko'rinishida yuboring\n"
        "3. Tasdiqlang yoki bekor qiling\n\n"
        "📋 <b>Mening vazifalarim:</b>\n"
        "Barcha vazifalaringizni ko'ring\n\n"
        "⏳ <b>Kutilayotgan vazifalar:</b>\n"
        "Hali bajarilmagan vazifalaringiz\n\n"
        "✅ <b>Bajarilgan vazifalar:</b>\n"
        "Bajarilgan vazifalaringiz\n\n"
        "👤 <b>Profil:</b>\n"
        "Shaxsiy ma'lumotlaringiz\n\n"
        "📞 <b>Savollar:</b>\n"
        "Muammo bo'lsa, administrator bilan bog'laning."
    )

    await message.answer(help_text, parse_mode='HTML', reply_markup=get_main_menu())
