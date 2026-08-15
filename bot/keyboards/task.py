from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_collecting_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='✅ Tasdiqlash', callback_data='confirm_tasks')],
            [InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel_task')],
        ]
    )
    return keyboard


def get_task_action_keyboard(task_id: int):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👁 Ko'rish", callback_data=f'view_task:{task_id}'),
                InlineKeyboardButton(text='✅ Bajarildi', callback_data=f'complete_task:{task_id}'),
            ],
        ]
    )
    return keyboard


def get_task_detail_keyboard(task_id: int):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='⬅️ Orqaga', callback_data='back_to_tasks')],
        ]
    )
    return keyboard
