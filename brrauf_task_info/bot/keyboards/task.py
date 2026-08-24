from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_collecting_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='✅ Tasdiqlash', callback_data='confirm_tasks')],
            [InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel_task')],
        ]
    )
    return keyboard


def get_confirm_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='✅ Tasdiqlash', callback_data='final_confirm')],
            [InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel_task')],
        ]
    )
    return keyboard


def get_responsible_keyboard(users: list[dict], recent_ids: list[int] = None):
    if recent_ids is None:
        recent_ids = []
    recent_set = set(recent_ids)
    buttons = []
    for u in users:
        prefix = "⭐ " if u['id'] in recent_set else ""
        buttons.append([
            InlineKeyboardButton(
                text=f"{prefix}{u['full_name']}",
                callback_data=f"select_responsible:{u['id']}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text='🔍 Qidirish', callback_data='search_responsible')
    ])
    buttons.append([
        InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel_task')
    ])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_search_results_keyboard(users: list[dict], recent_ids: list[int] = None):
    if recent_ids is None:
        recent_ids = []
    recent_set = set(recent_ids)
    buttons = []
    for u in users:
        prefix = "⭐ " if u['id'] in recent_set else ""
        buttons.append([
            InlineKeyboardButton(
                text=f"{prefix}{u['full_name']}",
                callback_data=f"select_responsible:{u['id']}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text='🔍 Qayta qidirish', callback_data='search_responsible')
    ])
    buttons.append([
        InlineKeyboardButton(text='⬅️ Orqaga', callback_data='back_to_responsible_list')
    ])
    buttons.append([
        InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel_task')
    ])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_search_cancel_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel_search')]
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
