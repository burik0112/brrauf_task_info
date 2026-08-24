import asyncio
import hashlib
import html
import logging

from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from asgiref.sync import sync_to_async
from django.conf import settings
from django.utils import timezone

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

MAX_COLLECTED_TASKS = 50
MAX_TITLE_LENGTH = 500
TELEGRAM_MAX_TEXT = 4096
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

_confirm_locks: dict[int, asyncio.Lock] = {}


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
        title = task['title'][:MAX_TITLE_LENGTH]
        lines.append(f"{i}. {icon} {html.escape(title)}")

    if len(tasks) >= MAX_COLLECTED_TASKS:
        lines.append(f"\n⚠️ Maksimal {MAX_COLLECTED_TASKS} ta vazifa. Tasdiqlang yoki bekor qiling.")
    else:
        lines.append("\nYana yuboring yoki tasdiqlang.")

    result = '\n'.join(lines)
    if len(result) > TELEGRAM_MAX_TEXT:
        result = result[:TELEGRAM_MAX_TEXT - 20] + "\n\n... (ro'yxat qisqartirildi)"
    return result


def format_task_for_confirm(tasks: list[dict], responsible_name: str) -> str:
    lines = [f"👤 <b>Mas'ul:</b> {html.escape(responsible_name)}\n"]
    lines.append("📋 <b>Vazifalar:</b>\n")
    for i, task in enumerate(tasks, 1):
        icon = SOURCE_ICONS.get(task['source'], '📄')
        lines.append(f"{i}. {icon} {html.escape(task['title'])}")
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

        if len(collected) >= MAX_COLLECTED_TASKS:
            return

        collected.append({'title': task_text[:MAX_TITLE_LENGTH], 'source': 'text'})
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

        if len(collected) >= MAX_COLLECTED_TASKS:
            return

        file_size = message.voice.file_size or 0
        if file_size > MAX_FILE_SIZE:
            size_mb = file_size // (1024 * 1024)
            await message.answer(
                f"❌ Fayl juda katta ({size_mb} MB). Maksimal {MAX_FILE_SIZE // (1024 * 1024)} MB.",
                reply_markup=get_collecting_keyboard(),
            )
            return

        duration = message.voice.duration or 0
        title = message.caption or f"Ovozli xabar ({duration}s)"
        collected.append({
            'title': title[:MAX_TITLE_LENGTH],
            'source': 'voice',
            'file_id': message.voice.file_id,
            'file_size': file_size,
        })
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

        if len(collected) >= MAX_COLLECTED_TASKS:
            return

        file_size = message.video.file_size or 0
        if file_size > MAX_FILE_SIZE:
            size_mb = file_size // (1024 * 1024)
            await message.answer(
                f"❌ Fayl juda katta ({size_mb} MB). Maksimal {MAX_FILE_SIZE // (1024 * 1024)} MB.",
                reply_markup=get_collecting_keyboard(),
            )
            return

        duration = message.video.duration or 0
        title = message.caption or f"Video xabar ({duration}s)"
        collected.append({
            'title': title[:MAX_TITLE_LENGTH],
            'source': 'video',
            'file_id': message.video.file_id,
            'file_size': file_size,
        })
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception:
        logger.exception('Error in collect_video_task')
        await message.answer("Xatolik yuz berdi.")


@router.message(TaskState.collecting_tasks, F.photo)
async def collect_photo_task(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        collected = data.get('collected_tasks', [])

        if len(collected) >= MAX_COLLECTED_TASKS:
            return

        caption = message.caption.strip() if message.caption else None
        title = (caption or 'Rasm')[:MAX_TITLE_LENGTH]
        media_group_id = message.media_group_id
        new_file = {'file_id': message.photo[-1].file_id, 'file_size': message.photo[-1].file_size or 0}

        if media_group_id and collected:
            last = collected[-1]
            if last.get('media_group_id') == media_group_id and last.get('source') == 'photo':
                last.setdefault('files', []).append(new_file)
                await state.update_data(collected_tasks=collected)
                await update_list_message(message, state, format_collected_tasks(collected))
                return

        collected.append({
            'title': title,
            'source': 'photo',
            'media_group_id': media_group_id,
            'files': [new_file],
        })
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

        if len(collected) >= MAX_COLLECTED_TASKS:
            return

        file_size = message.video_note.file_size or 0
        if file_size > MAX_FILE_SIZE:
            size_mb = file_size // (1024 * 1024)
            await message.answer(
                f"❌ Fayl juda katta ({size_mb} MB). Maksimal {MAX_FILE_SIZE // (1024 * 1024)} MB.",
                reply_markup=get_collecting_keyboard(),
            )
            return

        duration = message.video_note.duration or 0
        title = message.caption or f"Video xabar - dumaloq ({duration}s)"
        collected.append({
            'title': title[:MAX_TITLE_LENGTH],
            'source': 'video_note',
            'file_id': message.video_note.file_id,
            'file_size': file_size,
        })
        await state.update_data(collected_tasks=collected)

        await update_list_message(message, state, format_collected_tasks(collected))
    except Exception:
        logger.exception('Error in collect_video_note_task')
        await message.answer("Xatolik yuz berdi.")


@router.callback_query(F.data == 'confirm_tasks', TaskState.collecting_tasks)
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
            lambda: list(dict.fromkeys(
                Task.objects.filter(telegram_user=user)
                .exclude(responsible_bitrix_id__isnull=True)
                .order_by('-created_at')
                .values_list('responsible_bitrix_id', flat=True)[:50]
            ))[:5]
        )()

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

        await state.set_state(TaskState.waiting_for_responsible)
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


@router.callback_query(F.data.startswith('select_responsible:'), StateFilter(TaskState.waiting_for_responsible, TaskState.waiting_for_responsible_search))
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
        await state.set_state(TaskState.confirming_tasks)
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


@router.callback_query(F.data == 'final_confirm', TaskState.confirming_tasks)
async def final_confirm(callback: CallbackQuery, state: FSMContext):
    chat_id = callback.message.chat.id
    lock = _confirm_locks.setdefault(chat_id, asyncio.Lock())
    async with lock:
        try:
            data = await state.get_data()

            if data.get('final_confirm_processed'):
                await callback.answer("Allaqachon qayta ishlandi.", show_alert=True)
                return

            collected = data.get('collected_tasks', [])
            list_msg_id = data.get('list_message_id')
            responsible_bitrix_id = data.get('responsible_bitrix_id')
            responsible_name = data.get('responsible_name')

            if not collected:
                await callback.answer("Vazifalar yo'q.")
                return

            idempotency_key = hashlib.sha256(
                f"{chat_id}:{responsible_bitrix_id}:{len(collected)}:{','.join(t['title'][:50] for t in collected)}".encode()
            ).hexdigest()[:64]

            existing = await sync_to_async(
                lambda: Task.objects.filter(idempotency_key=idempotency_key).exists()
            )()
            if existing:
                await state.update_data(final_confirm_processed=True)
                await callback.answer("Allaqachon qayta ishlandi.", show_alert=True)
                return

            await state.update_data(final_confirm_processed=True)

            await callback.message.edit_reply_markup(reply_markup=None)
            try:
                await callback.answer()
            except Exception:
                pass

            user = await sync_to_async(TelegramUser.objects.get)(
                telegram_id=callback.from_user.id
            )

            tasks_to_create = [
                Task(
                    telegram_user=user,
                    title=item['title'][:MAX_TITLE_LENGTH],
                    responsible_bitrix_id=responsible_bitrix_id,
                    responsible_name=responsible_name,
                    status=Task.Status.PENDING,
                    source=item['source'],
                    telegram_file_id=item.get('file_id', ''),
                    idempotency_key=idempotency_key,
                )
                for item in collected
            ]
            tasks_saved = await sync_to_async(Task.objects.bulk_create)(tasks_to_create)

            bitrix_task_id = None
            bitrix_url = None
            bitrix_error_msg = None
            attachment_errors = []
            if user.bitrix_id and responsible_bitrix_id:
                creator_name = f"{user.bitrix_first_name or ''} {user.bitrix_last_name or ''}".strip() or str(user.telegram_id)
                today = timezone.localdate().strftime('%d.%m.%Y')
                task_title = f"{today} — {creator_name} → {responsible_name}"

                task_description = '\n'.join([f"{i+1}. {item['title']}" for i, item in enumerate(collected)])

                bitrix_result = await bitrix_service.create_task(
                    title=task_title,
                    creator_id=user.bitrix_id,
                    responsible_id=responsible_bitrix_id,
                    description=task_description,
                )
                if bitrix_result.get('ok'):
                    bitrix_task_id = int(bitrix_result['id'])
                    bitrix_url = f"{settings.BITRIX_PORTAL_URL}/company/personal/user/{user.bitrix_id}/tasks/task/view/{bitrix_task_id}/"
                    for task in tasks_saved:
                        task.bitrix_task_id = bitrix_task_id
                        task.bitrix_synced = True
                    await sync_to_async(Task.objects.bulk_update)(tasks_saved, ['bitrix_task_id', 'bitrix_synced'])

                    try:
                        for i, item in enumerate(collected):
                            files = item.get('files', [{'file_id': item.get('file_id'), 'file_size': item.get('file_size', 0)}])
                            for j, f in enumerate(files):
                                file_id = f.get('file_id')
                                if not file_id:
                                    continue
                                file_size = f.get('file_size', 0)
                                if file_size > MAX_FILE_SIZE:
                                    size_mb = file_size // (1024 * 1024)
                                    label = f"{i+1}" if len(files) == 1 else f"{i+1}.{j+1}"
                                    attachment_errors.append(f"{label}. {item['title'][:30]} ({size_mb} MB - hajm juda katta)")
                                    continue
                                try:
                                    file_info = await callback.message.bot.get_file(file_id)
                                    file_content = await callback.message.bot.download_file(file_info.file_path)
                                    ext = file_info.file_path.split('.')[-1]
                                    file_name = f"{item['source']}.{ext}"
                                    attach_ok = await bitrix_service.attach_file_to_task(
                                        task_id=bitrix_task_id,
                                        file_name=file_name,
                                        file_content=file_content.getvalue(),
                                    )
                                    if not attach_ok:
                                        label = f"{i+1}" if len(files) == 1 else f"{i+1}.{j+1}"
                                        attachment_errors.append(f"{label}. {item['title'][:30]} (Bitrix'ga yuklashda xato)")
                                except Exception as e:
                                    logger.exception(f"Error attaching file to Bitrix task: {bitrix_task_id}")
                                    label = f"{i+1}" if len(files) == 1 else f"{i+1}.{j+1}"
                                    attachment_errors.append(f"{label}. {item['title'][:30]} (xato: {str(e)[:50]})")
                    except Exception:
                        logger.exception("Unexpected error in attachment loop")
                else:
                    bitrix_error_msg = bitrix_result.get('error', 'Noma\'lum xato')
                    for task in tasks_saved:
                        task.bitrix_error = bitrix_error_msg
                    await sync_to_async(Task.objects.bulk_update)(tasks_saved, ['bitrix_error'])
            elif not user.bitrix_id:
                bitrix_error_msg = "Bitrix ID kiritilmagan"
            elif not responsible_bitrix_id:
                bitrix_error_msg = "Mas'ul tanlanmagan"

            task_list = '\n'.join([f"{i+1}. {html.escape(t.title)}" for i, t in enumerate(tasks_saved)])

            if bitrix_url:
                status_line = f"✅ <b>{len(tasks_saved)} ta vazifa Bitrix24 ga yuborildi!</b>\n\n"
                bitrix_link = f"\n\n🔗 Bitrix task:\n{bitrix_url}"
            else:
                status_line = f"⚠️ <b>{len(tasks_saved)} ta vazifa faqat lokal saqlandi</b>\n"
                bitrix_link = f"\n\n❌ Bitrix24 ga yuborilmadi: {html.escape(bitrix_error_msg)}"

            attachment_warning = ""
            if attachment_errors:
                attachment_warning = "\n\n⚠️ <b>Fayllar yuklanmadi:</b>\n" + '\n'.join(html.escape(e) for e in attachment_errors)

            text = (
                f"{status_line}\n"
                f"👤 Mas'ul: {html.escape(responsible_name or '')}\n\n"
                f"{task_list}"
                f"{bitrix_link}"
                f"{attachment_warning}"
            )

            if len(text) > TELEGRAM_MAX_TEXT:
                text = text[:TELEGRAM_MAX_TEXT - 20] + "\n\n... (xabar qisqartirildi)"

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


@router.callback_query(F.data == 'cancel_task', StateFilter(TaskState.collecting_tasks, TaskState.waiting_for_responsible, TaskState.waiting_for_responsible_search, TaskState.confirming_tasks))
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
                f"❌ \"{html.escape(query)}\" bo'yicha hech kim topilmadi.\n"
                "Boshqa ism yozing yoki bekor qiling.",
                reply_markup=get_search_cancel_keyboard(),
            )
            return

        data = await state.get_data()
        recent_ids = data.get('recent_ids', [])

        await state.update_data(search_results=users)

        search_msg = await message.answer(
            f"🔍 <b>\"{html.escape(query)}\" natijalari ({len(users)} ta):</b>",
            parse_mode='HTML',
            reply_markup=get_search_results_keyboard(users, recent_ids),
        )
        await state.update_data(list_message_id=search_msg.message_id)
    except Exception:
        logger.exception('Error in process_search')
        await message.answer("Xatolik yuz berdi.")


@router.callback_query(F.data == 'back_to_responsible_list', StateFilter(TaskState.waiting_for_responsible, TaskState.waiting_for_responsible_search))
async def back_to_responsible_list(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        users = data.get('bitrix_users', [])
        recent_ids = data.get('recent_ids', [])

        await state.set_state(TaskState.waiting_for_responsible)
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


@router.callback_query(F.data == 'cancel_search', TaskState.waiting_for_responsible_search)
async def cancel_search(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        users = data.get('bitrix_users', [])
        recent_ids = data.get('recent_ids', [])

        await state.set_state(TaskState.waiting_for_responsible)
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


@router.callback_query(F.data.startswith(('select_responsible:', 'confirm_tasks', 'final_confirm', 'cancel_task', 'back_to_responsible_list', 'cancel_search')))
async def expired_session_callback(callback: CallbackQuery):
    await callback.answer(
        "Sessiya eskirgan. Qaytadan boshlash uchun /start ni bosing.",
        show_alert=True,
    )
