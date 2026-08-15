from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async
import logging

from users.models import TelegramUser
from tasks.models import Task
from bot.keyboards.main_menu import get_main_menu
from bot.keyboards.task import get_task_detail_keyboard

router = Router()
logger = logging.getLogger(__name__)


def format_task_list(tasks, title):
    if not tasks:
        return f"📭 <b>{title}</b>\n\nSizda hozircha vazifalar mavjud emas."

    lines = [f"📋 <b>{title}</b>\n"]
    for i, task in enumerate(tasks[:10], 1):
        status_emoji = '🟡' if task.status == 'pending' else '🟢'
        lines.append(f"{i}️⃣ {status_emoji} {task.title[:50]}")
    return '\n\n'.join(lines)


@router.message(F.text == '📋 Mening vazifalarim')
async def my_tasks(message: Message, state: FSMContext):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id, is_registered=True
        )
        tasks = await sync_to_async(list)(
            Task.objects.filter(telegram_user=user)
        )
        await message.answer(
            format_task_list(tasks, '📋 Mening vazifalarim'),
            parse_mode='HTML', reply_markup=get_main_menu()
        )
    except TelegramUser.DoesNotExist:
        await message.answer(
            "Siz hali ro'yxatdan o'tmaganishingiz.\n"
            "/start buyrug'ini bosing.",
            reply_markup=get_main_menu(),
        )
    except Exception as e:
        logger.exception('Error in my_tasks')
        await message.answer("Xatolik yuz berdi.")


@router.message(F.text == '⏳ Kutilayotgan vazifalar')
async def pending_tasks(message: Message, state: FSMContext):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id, is_registered=True
        )
        tasks = await sync_to_async(list)(
            Task.objects.filter(telegram_user=user, status='pending')
        )
        await message.answer(
            format_task_list(tasks, '⏳ Kutilayotgan vazifalar'),
            parse_mode='HTML', reply_markup=get_main_menu()
        )
    except TelegramUser.DoesNotExist:
        await message.answer("Ro'yxatdan o'tmagan. /start bosing.", reply_markup=get_main_menu())
    except Exception as e:
        logger.exception('Error in pending_tasks')
        await message.answer("Xatolik yuz berdi.")


@router.message(F.text == '✅ Bajarilgan vazifalar')
async def completed_tasks(message: Message, state: FSMContext):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id, is_registered=True
        )
        tasks = await sync_to_async(list)(
            Task.objects.filter(telegram_user=user, status='completed')
        )
        await message.answer(
            format_task_list(tasks, '✅ Bajarilgan vazifalar'),
            parse_mode='HTML', reply_markup=get_main_menu()
        )
    except TelegramUser.DoesNotExist:
        await message.answer("Ro'yxatdan o'tmagan. /start bosing.", reply_markup=get_main_menu())
    except Exception as e:
        logger.exception('Error in completed_tasks')
        await message.answer("Xatolik yuz berdi.")


@router.callback_query(F.data.startswith('view_task:'))
async def view_task(callback: CallbackQuery, state: FSMContext):
    try:
        task_id = int(callback.data.split(':')[1])
        task = await sync_to_async(Task.objects.get)(
            id=task_id, telegram_user__telegram_id=callback.from_user.id
        )

        await callback.message.edit_text(
            f"📋 <b>Vazifa</b>\n\n"
            f"📝 <b>Nomi:</b>\n{task.title}\n\n"
            f"📊 <b>Status:</b> {task.get_status_display()}\n\n"
            f"📥 <b>Manba:</b> {task.get_source_display()}\n"
            f"📅 <b>Yaratilgan:</b> {task.created_at.strftime('%d.%m.%Y %H:%M')}",
            parse_mode='HTML',
            reply_markup=get_task_detail_keyboard(task.id),
        )
        await callback.answer()
    except Task.DoesNotExist:
        await callback.message.answer("Vazifa topilmadi.")
        await callback.answer()
    except Exception as e:
        logger.exception('Error in view_task')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()


@router.callback_query(F.data.startswith('complete_task:'))
async def complete_task(callback: CallbackQuery, state: FSMContext):
    try:
        task_id = int(callback.data.split(':')[1])
        task = await sync_to_async(Task.objects.get)(
            id=task_id, telegram_user__telegram_id=callback.from_user.id
        )
        task.status = 'completed'
        await sync_to_async(task.save)()

        await callback.message.edit_text(
            f"✅ <b>Vazifa bajarildi!</b>\n\n"
            f"📝 {task.title}\n\nAsosiy menyudan foydalaning:",
            parse_mode='HTML',
        )
        await callback.message.answer("Menyu:", reply_markup=get_main_menu())
        await callback.answer()
    except Task.DoesNotExist:
        await callback.message.answer("Vazifa topilmadi.")
        await callback.answer()
    except Exception as e:
        logger.exception('Error in complete_task')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()


@router.callback_query(F.data == 'back_to_tasks')
async def back_to_tasks(callback: CallbackQuery, state: FSMContext):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=callback.from_user.id
        )
        tasks = await sync_to_async(list)(
            Task.objects.filter(telegram_user=user)
        )
        await callback.message.edit_text(
            format_task_list(tasks, '📋 Mening vazifalarim'),
            parse_mode='HTML'
        )
        await callback.answer()
    except Exception as e:
        logger.exception('Error in back_to_tasks')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()
