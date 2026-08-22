from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='📋 Vazifa yaratish')],
        ],
        resize_keyboard=True,
    )
    return keyboard
