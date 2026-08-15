from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async
import logging

from users.models import TelegramUser
from tasks.models import Task
from bot.states.task import TaskState
from bot.keyboards.main_menu import get_main_menu
from bot.keyboards.task import get_collecting_keyboard

router = Router()
logger = logging.getLogger(__name__)


def format_collected_tasks(tasks: list[dict]) -> str:
    if not tasks:
        return "📭 Vazifalar yo'q."

    lines = [f"📋 <b>Yig'ilgan vazifalar ({len(tasks)} ta):</b>\n"]
    for i, task in enumerate(tasks, 1):
        source_icon = '🎤' if task['source'] == 'voice' else '📝'
        lines.append(f"{i}️⃣ {source_icon} {task['title']}")
    lines.append("\nYana yuboring yoki tasdiqlang.")
    return '\n'.join(lines)


async def update_list_message(message: Message, state: FSMContext, text: str):
    data = await state.get_data()
    list_msg_id = data.get('list_message_id')

    if list_msg_id:
        try:
            await message.bot.edit_message_text(
                text=text,
                chat_id=message.chat.id,
                message_id=list_msg_id,
                parse_mode='HTML',
                reply_markup=get_collecting_keyboard(),
            )
            return
        except Exception:
            pass

    msg = await message.answer(
        text=text,
        parse_mode='HTML',
        reply_markup=get_collecting_keyboard(),
    )
    await state.update_data(list_message_id=msg.message_id)


@router.message(F.text == '📋 Vazifa yaratish')
async def create_task(message: Message, state: FSMContext):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=message.from_user.id, is_registered=True
        )
        await state.update_data(collected_tasks=[], list_message_id=None)

        await message.answer(
            "📋 <b>Vazifalarni yuboring</b>\n\n"
            "Matn yoki ovozli xabar yuboring.\n"
            "Tayyor bo'lgach, <b>✅ Tasdiqlash</b> tugmasini bosing.",
            parse_mode='HTML',
        )
        await state.set_state(TaskState.collecting_tasks)
    except TelegramUser.DoesNotExist:
        await message.answer(
            "Siz hali ro'yxatdan o'tmaganishingiz.\n"
            "/start buyrug'ini bosing.",
            reply_markup=get_main_menu(),
        )
    except Exception as e:
        logger.exception('Error in create_task')
        await message.answer("Xatolik yuz berdi.")


@router.message(TaskState.collecting_tasks, F.text)
async def collect_text_task(message: Message, state: FSMContext):
    try:
        task_text = message.text.strip()
        if not task_text:
            return

        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        collected.append({'title': task_text, 'source': 'text'})
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception as e:
        logger.exception('Error in collect_text_task')
        await message.answer("Xatolik yuz berdi.")


@router.message(TaskState.collecting_tasks, F.voice)
async def collect_voice_task(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        collected.append({'title': 'Ovozli vazifa', 'source': 'voice'})
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception as e:
        logger.exception('Error in collect_voice_task')
        await message.answer("Xatolik yuz berdi.")


@router.callback_query(F.data == 'confirm_tasks')
async def confirm_tasks(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        list_msg_id = data.get('list_message_id')

        if not collected:
            await callback.answer("Vazifalar yo'q.")
            return

        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=callback.from_user.id
        )

        tasks = []
        for item in collected:
            task = await sync_to_async(Task.objects.create)(
                telegram_user=user,
                title=item['title'],
                status=Task.Status.PENDING,
                source=item['source'],
            )
            tasks.append(task)

        task_list = '\n'.join([f"{i+1}. {t.title}" for i, t in enumerate(tasks)])
        text = f"✅ <b>{len(tasks)} ta vazifa saqlandi!</b>\n\n{task_list}"

        if list_msg_id:
            try:
                await callback.message.bot.edit_message_text(
                    text=text,
                    chat_id=callback.message.chat.id,
                    message_id=list_msg_id,
                    parse_mode='HTML',
                )
            except Exception:
                await callback.message.answer(text, parse_mode='HTML')
        else:
            await callback.message.answer(text, parse_mode='HTML')

        await callback.message.answer("Menyu:", reply_markup=get_main_menu())
        await state.clear()
        await callback.answer()
    except Exception as e:
        logger.exception('Error in confirm_tasks')
        await callback.message.answer("Xatolik yuz berdi.")
        await state.clear()
        await callback.answer()


@router.callback_query(F.data == 'cancel_task')
async def cancel_task(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        list_msg_id = data.get('list_message_id')
        count = len(collected)

        text = f"❌ <b>Bekor qilindi.</b> ({count} ta saqlanmadi)"

        if list_msg_id:
            try:
                await callback.message.bot.edit_message_text(
                    text=text,
                    chat_id=callback.message.chat.id,
                    message_id=list_msg_id,
                    parse_mode='HTML',
                )
            except Exception:
                await callback.message.answer(text, parse_mode='HTML')
        else:
            await callback.message.answer(text, parse_mode='HTML')

        await callback.message.answer("Menyu:", reply_markup=get_main_menu())
        await state.clear()
        await callback.answer()
    except Exception as e:
        logger.exception('Error in cancel_task')
        await callback.message.answer("Xatolik yuz berdi.")
        await state.clear()
        await callback.answer()
