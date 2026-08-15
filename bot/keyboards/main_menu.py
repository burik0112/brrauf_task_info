from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='📋 Vazifa yaratish')],
            [
                KeyboardButton(text='📋 Mening vazifalarim'),
                KeyboardButton(text='⏳ Kutilayotgan vazifalar'),
            ],
            [
                KeyboardButton(text='✅ Bajarilgan vazifalar'),
                KeyboardButton(text='👤 Profil'),
            ],
            [KeyboardButton(text='ℹ️ Yordam')],
        ],
        resize_keyboard=True,
    )
    return keyboard
