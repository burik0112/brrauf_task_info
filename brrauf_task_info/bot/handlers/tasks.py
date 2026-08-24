import datetime
import logging

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from asgiref.sync import sync_to_async

from bot.keyboards.main_menu import get_main_menu
from bot.keyboards.task import (
    get_collecting_keyboard,
    get_confirm_keyboard,
    get_responsible_keyboard,
    get_search_cancel_keyboard,
    get_search_results_keyboard,
)
from bot.states.task import TaskState
from tasks.models import Task
from tasks.services import bitrix_service
from users.models import TelegramUser

router = Router()
logger = logging.getLogger(__name__)


SOURCE_ICONS = {
    'text': '📝',
    'voice': '🎤',
    'video': '🎬',
    'photo': '🖼',
    'video_note': '📹',
}


def format_collected_tasks(tasks: list[dict]) -> str:
    if not tasks:
        return "📭 Vazifalar yo'q."

    lines = [f"📋 <b>Yig'ilgan vazifalar ({len(tasks)} ta):</b>\n"]
    for i, task in enumerate(tasks, 1):
        icon = SOURCE_ICONS.get(task['source'], '📄')
        lines.append(f"{i}️⃣ {icon} {task['title']}")
    lines.append("\nYana yuboring yoki tasdiqlang.")
    return '\n'.join(lines)


def format_task_for_confirm(tasks: list[dict], responsible_name: str) -> str:
    lines = [f"👤 <b>Mas'ul:</b> {responsible_name}\n"]
    lines.append("📋 <b>Vazifalar:</b>\n")
    for i, task in enumerate(tasks, 1):
        icon = SOURCE_ICONS.get(task['source'], '📄')
        lines.append(f"{i}️⃣ {icon} {task['title']}")
    lines.append("\nTasdiqlaysizmi?")
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
        _user = await sync_to_async(TelegramUser.objects.get)(
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
    except Exception:
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
    except Exception:
        logger.exception('Error in collect_text_task')
        await message.answer("Xatolik yuz berdi.")


@router.message(TaskState.collecting_tasks, F.voice)
async def collect_voice_task(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        collected.append({'title': 'Ovozli vazifa', 'source': 'voice', 'file_id': message.voice.file_id})
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception:
        logger.exception('Error in collect_voice_task')
        await message.answer("Xatolik yuz berdi.")


@router.message(TaskState.collecting_tasks, F.video)
async def collect_video_task(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        collected.append({'title': 'Video xabar', 'source': 'video', 'file_id': message.video.file_id})
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception:
        logger.exception('Error in collect_video_task')
        await message.answer("Xatolik yuz berdi.")


@router.message(TaskState.collecting_tasks, F.photo)
async def collect_photo_task(message: Message, state: FSMContext):
    try:
        caption = message.caption
        title = caption if caption else 'Rasm'
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        collected.append({'title': title, 'source': 'photo', 'file_id': message.photo[-1].file_id})
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception:
        logger.exception('Error in collect_photo_task')
        await message.answer("Xatolik yuz berdi.")


@router.message(TaskState.collecting_tasks, F.video_note)
async def collect_video_note_task(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        collected.append({'title': 'Video xabar (dumaloq)', 'source': 'video_note', 'file_id': message.video_note.file_id})
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception:
        logger.exception('Error in collect_video_note_task')
        await message.answer("Xatolik yuz berdi.")


@router.callback_query(F.data == 'confirm_tasks')
async def confirm_tasks(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])

        if not collected:
            await callback.answer("Vazifalar yo'q.")
            return

        await callback.message.edit_text(
            "⏳ Bitrix24 dan foydalanuvchilar olinmoqda...",
            parse_mode='HTML',
        )

        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=callback.from_user.id
        )

        recent_ids = await sync_to_async(
            lambda: list(
                Task.objects.filter(telegram_user=user)
                .exclude(responsible_bitrix_id__isnull=True)
                .order_by('-created_at')
                .values_list('responsible_bitrix_id', flat=True)
                .distinct()[:5]
            )
        )()

        last_responsible_id = await sync_to_async(
            lambda: Task.objects.filter(
                telegram_user=user,
                responsible_bitrix_id__isnull=False,
            ).order_by('-created_at').values_list('responsible_bitrix_id', flat=True).first()
        )()

        if last_responsible_id and last_responsible_id not in recent_ids:
            recent_ids.insert(0, last_responsible_id)
        elif last_responsible_id and recent_ids and recent_ids[0] != last_responsible_id:
            recent_ids.remove(last_responsible_id)
            recent_ids.insert(0, last_responsible_id)

        users = await bitrix_service.get_top_users(recent_ids, limit=10)
        if not users:
            await callback.message.edit_text(
                "❌ Bitrix24 dan foydalanuvchilar olinmadi.\n"
                "Qaytadan urinib ko'ring.",
                parse_mode='HTML',
            )
            await callback.answer()
            return

        await state.update_data(bitrix_users=users, recent_ids=recent_ids)

        await callback.message.edit_text(
            "👤 <b>Mas'ulni tanlang:</b>",
            parse_mode='HTML',
            reply_markup=get_responsible_keyboard(users, recent_ids),
        )
        await callback.answer()
    except Exception:
        logger.exception('Error in confirm_tasks')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()


@router.callback_query(F.data.startswith('select_responsible:'))
async def select_responsible(callback: CallbackQuery, state: FSMContext):
    try:
        bitrix_id = int(callback.data.split(':')[1])

        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        users = data.get('bitrix_users', [])
        search_results = data.get('search_results', [])

        all_users = {u['id']: u for u in users}
        for u in search_results:
            if u['id'] not in all_users:
                all_users[u['id']] = u

        responsible = all_users.get(bitrix_id)
        if not responsible:
            await callback.answer("Foydalanuvchi topilmadi.")
            return

        await state.update_data(
            responsible_bitrix_id=bitrix_id,
            responsible_name=responsible['full_name'],
            list_message_id=callback.message.message_id,
        )

        confirm_text = format_task_for_confirm(collected, responsible['full_name'])
        await callback.message.edit_text(
            confirm_text,
            parse_mode='HTML',
            reply_markup=get_confirm_keyboard(),
        )
        await callback.answer()
    except Exception:
        logger.exception('Error in select_responsible')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()


@router.callback_query(F.data == 'final_confirm')
async def final_confirm(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])
        list_msg_id = data.get('list_message_id')
        responsible_bitrix_id = data.get('responsible_bitrix_id')
        responsible_name = data.get('responsible_name')

        if not collected:
            await callback.answer("Vazifalar yo'q.")
            return

        await callback.message.edit_reply_markup(reply_markup=None)
        try:
            await callback.answer()
        except Exception:
            pass

        user = await sync_to_async(TelegramUser.objects.get)(
            telegram_id=callback.from_user.id
        )

        tasks_saved = []
        for item in collected:
            task = await sync_to_async(Task.objects.create)(
                telegram_user=user,
                title=item['title'],
                responsible_bitrix_id=responsible_bitrix_id,
                responsible_name=responsible_name,
                status=Task.Status.PENDING,
                source=item['source'],
            )
            tasks_saved.append(task)

        bitrix_task_id = None
        bitrix_url = None
        if user.bitrix_id and responsible_bitrix_id:
            creator_name = f"{user.bitrix_first_name or ''} {user.bitrix_last_name or ''}".strip() or str(user.telegram_id)
            today = datetime.date.today().strftime('%d.%m.%Y')
            task_title = f"{today} — {creator_name} → {responsible_name}"

            task_description = '\n'.join([f"{i+1}. {item['title']}" for i, item in enumerate(collected)])

            bitrix_result = await bitrix_service.create_task(
                title=task_title,
                creator_id=user.bitrix_id,
                responsible_id=responsible_bitrix_id,
                description=task_description,
            )
            if bitrix_result:
                bitrix_task_id = bitrix_result['id']
                bitrix_url = f"https://brrauf.bitrix24.uz/company/personal/user/{user.bitrix_id}/tasks/task/view/{bitrix_task_id}/"
                for task in tasks_saved:
                    task.bitrix_task_id = bitrix_task_id
                    await sync_to_async(task.save)()

                for item in collected:
                    if item.get('file_id'):
                        try:
                            file_info = await callback.message.bot.get_file(item['file_id'])
                            file_content = await callback.message.bot.download_file(file_info.file_path)
                            ext = file_info.file_path.split('.')[-1]
                            file_name = f"{item['source']}.{ext}"
                            await bitrix_service.attach_file_to_task(
                                task_id=bitrix_task_id,
                                file_name=file_name,
                                file_content=file_content.getvalue(),
                            )
                        except Exception:
                            logger.exception(f"Error attaching file to Bitrix task: {bitrix_task_id}")

        task_list = '\n'.join([f"{i+1}. {t.title}" for i, t in enumerate(tasks_saved)])
        bitrix_link = f"\n\n🔗 Bitrix task:\n{bitrix_url}" if bitrix_url else ""

        text = (
            f"✅ <b>{len(tasks_saved)} ta vazifa saqlandi!</b>\n\n"
            f"👤 Mas'ul: {responsible_name}\n\n"
            f"{task_list}"
            f"{bitrix_link}"
        )

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
    except Exception:
        logger.exception('Error in final_confirm')
        await callback.message.answer("Xatolik yuz berdi.")
        await state.clear()


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
    except Exception:
        logger.exception('Error in cancel_task')
        await callback.message.answer("Xatolik yuz berdi.")
        await state.clear()
        await callback.answer()


@router.callback_query(F.data == 'search_responsible')
async def search_responsible(callback: CallbackQuery, state: FSMContext):
    try:
        await state.set_state(TaskState.waiting_for_responsible_search)
        await callback.message.edit_text(
            "🔍 <b>Mas'ul ismini yozing:</b>\n\n"
            "Ism yoki familiyani kiriting.",
            parse_mode='HTML',
            reply_markup=get_search_cancel_keyboard(),
        )
        await callback.answer()
    except Exception:
        logger.exception('Error in search_responsible')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()


@router.message(TaskState.waiting_for_responsible_search, F.text)
async def process_search(message: Message, state: FSMContext):
    try:
        query = message.text.strip()
        if not query or len(query) < 2:
            await message.answer(
                "Kamida 2 ta harf kiriting.",
                reply_markup=get_search_cancel_keyboard(),
            )
            return

        users = await bitrix_service.search_users(query, limit=10)

        if not users:
            await message.answer(
                f"❌ \"{query}\" bo'yicha hech kim topilmadi.\n"
                "Boshqa ism yozing yoki bekor qiling.",
                reply_markup=get_search_cancel_keyboard(),
            )
            return

        data = await state.get_data()
        recent_ids = data.get('recent_ids', [])

        await state.update_data(search_results=users)

        search_msg = await message.answer(
            f"🔍 <b>\"{query}\" natijalari ({len(users)} ta):</b>",
            parse_mode='HTML',
            reply_markup=get_search_results_keyboard(users, recent_ids),
        )
        await state.update_data(list_message_id=search_msg.message_id)
    except Exception:
        logger.exception('Error in process_search')
        await message.answer("Xatolik yuz berdi.")


@router.callback_query(F.data == 'back_to_responsible_list')
async def back_to_responsible_list(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        users = data.get('bitrix_users', [])
        recent_ids = data.get('recent_ids', [])

        await state.set_state(TaskState.collecting_tasks)
        await state.update_data(list_message_id=callback.message.message_id)

        await callback.message.edit_text(
            "👤 <b>Mas'ulni tanlang:</b>",
            parse_mode='HTML',
            reply_markup=get_responsible_keyboard(users, recent_ids),
        )
        await callback.answer()
    except Exception:
        logger.exception('Error in back_to_responsible_list')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()


@router.callback_query(F.data == 'cancel_search')
async def cancel_search(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        users = data.get('bitrix_users', [])
        recent_ids = data.get('recent_ids', [])

        await state.set_state(TaskState.collecting_tasks)
        await state.update_data(list_message_id=callback.message.message_id)

        await callback.message.edit_text(
            "👤 <b>Mas'ulni tanlang:</b>",
            parse_mode='HTML',
            reply_markup=get_responsible_keyboard(users, recent_ids),
        )
        await callback.answer()
    except Exception:
        logger.exception('Error in cancel_search')
        await callback.message.answer("Xatolik yuz berdi.")
        await callback.answer()
