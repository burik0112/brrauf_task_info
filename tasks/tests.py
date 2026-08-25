import asyncio
from unittest.mock import AsyncMock, patch, MagicMock

from django.test import TestCase, TransactionTestCase
from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    Chat, User, Message, CallbackQuery, Contact, PhotoSize, Voice, Video, Update,
)

from bot.handlers.tasks import router as tasks_router, _confirm_locks, MAX_FILE_SIZE
from bot.handlers.registration import router as registration_router
from bot.states.task import TaskState
from bot.states.registration import RegistrationState
from tasks.models import Task
from users.models import TelegramUser


BOT_ID = 1
CHAT_ID = 999
USER_ID = 111
KEY = StorageKey(bot_id=BOT_ID, user_id=USER_ID, chat_id=CHAT_ID)

_update_id_counter = 0


def _next_update_id():
    global _update_id_counter
    _update_id_counter += 1
    return _update_id_counter


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def _make_dp():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(tasks_router)
    dp.include_router(registration_router)
    return dp, storage


def _reset_router():
    tasks_router._parent_router = None
    registration_router._parent_router = None


def _make_bot():
    bot = AsyncMock(spec=Bot)
    bot.id = BOT_ID
    bot.__class__ = Bot
    return bot


def _user(telegram_id=USER_ID, username='testuser', first_name='Test', last_name='User'):
    return User(id=telegram_id, is_bot=False, first_name=first_name, last_name=last_name, username=username)


def _chat(chat_id=CHAT_ID):
    return Chat(id=chat_id, type='private')


def _msg(text='/start', user=None, chat=None, message_id=1):
    return Message(message_id=message_id, date=1234567890, chat=chat or _chat(),
                   from_user=user or _user(), text=text)


def _cb(data, user=None, chat=None, cb_msg_id=10):
    msg = Message(message_id=cb_msg_id, date=1234567890, chat=chat or _chat(),
                  from_user=user or _user(), text='')
    return CallbackQuery(id=f'cb{_next_update_id()}', from_user=user or _user(),
                         chat_instance='test', data=data, message=msg)


def _contact_msg(user_id, phone_number, user=None):
    return Message(message_id=1, date=1234567890, chat=_chat(),
                   from_user=user or _user(),
                   contact=Contact(user_id=user_id, phone_number=phone_number, first_name='T'))


def _photo_msg(file_id='p1', file_size=1024, media_group_id=None, caption=None):
    photo = PhotoSize(file_id=file_id, file_unique_id=f'{file_id}_u',
                      width=100, height=100, file_size=file_size)
    return Message(message_id=_next_update_id(), date=1234567890, chat=_chat(), from_user=_user(),
                   photo=[photo], caption=caption, media_group_id=media_group_id)


def _voice_msg(file_id='v1', file_size=5000, duration=10):
    return Message(message_id=_next_update_id(), date=1234567890, chat=_chat(), from_user=_user(),
                   voice=Voice(file_id=file_id, file_unique_id=f'{file_id}_u',
                               duration=duration, file_size=file_size))


def _video_msg(file_id='vid1', file_size=5000, duration=30):
    return Message(message_id=_next_update_id(), date=1234567890, chat=_chat(), from_user=_user(),
                   video=Video(file_id=file_id, file_unique_id=f'{file_id}_u',
                               duration=duration, file_size=file_size,
                               width=100, height=100))


async def _set_state(storage, state, data=None):
    ctx = FSMContext(storage=storage, key=KEY)
    await ctx.set_state(state)
    if data:
        await ctx.update_data(**data)
    return ctx


async def _get_state(storage):
    ctx = FSMContext(storage=storage, key=KEY)
    return await ctx.get_state()


async def _get_data(storage):
    ctx = FSMContext(storage=storage, key=KEY)
    return await ctx.get_data()


async def _feed(dp, bot, message_or_cb):
    if isinstance(message_or_cb, CallbackQuery):
        upd = Update(update_id=_next_update_id(), callback_query=message_or_cb)
    else:
        upd = Update(update_id=_next_update_id(), message=message_or_cb)
    return await dp.feed_update(bot, upd)


class ResponsibleSelectionFlowTest(TestCase):
    """AUDIT-02 regression: search results keyboard buttons must work."""

    def setUp(self):
        _confirm_locks.clear()
        _reset_router()
        self.dp, self.storage = _make_dp()
        self.bot = _make_bot()
        self.tg_user = TelegramUser.objects.create(
            telegram_id=USER_ID, username='testuser', first_name='Test', last_name='User',
            is_registered=True, bitrix_id=10, bitrix_first_name='Test', bitrix_last_name='User',
        )

    def _setup(self, state, data):
        return _run(_set_state(self.storage, state, data))

    def test_select_responsible_from_list(self):
        self._setup(TaskState.waiting_for_responsible, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 10,
            'bitrix_users': [{'id': 10, 'full_name': 'Alice', 'name': 'Alice', 'last_name': 'Smith'}],
            'recent_ids': [],
        })
        _run(_feed(self.dp, self.bot, _cb('select_responsible:10')))
        data = _run(_get_data(self.storage))
        self.assertEqual(data.get('responsible_bitrix_id'), 10)

    def test_select_responsible_from_search(self):
        self._setup(TaskState.waiting_for_responsible_search, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 20,
            'bitrix_users': [{'id': 10, 'full_name': 'Alice', 'name': 'Alice', 'last_name': 'Smith'}],
            'recent_ids': [],
            'search_results': [{'id': 20, 'full_name': 'Bob', 'name': 'Bob', 'last_name': 'Search'}],
        })
        _run(_feed(self.dp, self.bot, _cb('select_responsible:20')))
        data = _run(_get_data(self.storage))
        self.assertEqual(data.get('responsible_bitrix_id'), 20)
        self.assertEqual(data.get('responsible_name'), 'Bob')

    def test_select_responsible_unknown_id(self):
        self._setup(TaskState.waiting_for_responsible, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 10,
            'bitrix_users': [{'id': 10, 'full_name': 'Alice', 'name': 'Alice', 'last_name': 'Smith'}],
            'recent_ids': [],
        })
        _run(_feed(self.dp, self.bot, _cb('select_responsible:999')))
        state = _run(_get_state(self.storage))
        self.assertEqual(str(state), 'TaskState:waiting_for_responsible')

    def test_back_to_responsible_list_from_search(self):
        self._setup(TaskState.waiting_for_responsible_search, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 20,
            'bitrix_users': [{'id': 10, 'full_name': 'Alice', 'name': 'Alice', 'last_name': 'Smith'}],
            'recent_ids': [],
        })
        _run(_feed(self.dp, self.bot, _cb('back_to_responsible_list')))
        state = _run(_get_state(self.storage))
        self.assertEqual(str(state), 'TaskState:waiting_for_responsible')

    def test_cancel_task_from_responsible(self):
        self._setup(TaskState.waiting_for_responsible, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 10,
            'bitrix_users': [],
            'recent_ids': [],
        })
        _run(_feed(self.dp, self.bot, _cb('cancel_task')))
        state = _run(_get_state(self.storage))
        self.assertIsNone(state)

    def test_cancel_task_from_search(self):
        self._setup(TaskState.waiting_for_responsible_search, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 20,
            'bitrix_users': [],
            'recent_ids': [],
        })
        _run(_feed(self.dp, self.bot, _cb('cancel_task')))
        state = _run(_get_state(self.storage))
        self.assertIsNone(state)

    def test_search_responsible(self):
        self._setup(TaskState.waiting_for_responsible, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 10,
            'bitrix_users': [],
            'recent_ids': [],
        })
        _run(_feed(self.dp, self.bot, _cb('search_responsible')))
        state = _run(_get_state(self.storage))
        self.assertEqual(str(state), 'TaskState:waiting_for_responsible_search')

    def test_cancel_search(self):
        self._setup(TaskState.waiting_for_responsible_search, {
            'collected_tasks': [{'title': 'Task', 'source': 'text'}],
            'list_message_id': 20,
            'bitrix_users': [{'id': 10, 'full_name': 'Alice', 'name': 'Alice', 'last_name': 'Smith'}],
            'recent_ids': [],
        })
        _run(_feed(self.dp, self.bot, _cb('cancel_search')))
        state = _run(_get_state(self.storage))
        self.assertEqual(str(state), 'TaskState:waiting_for_responsible')

    def test_expired_session_callback(self):
        _run(_feed(self.dp, self.bot, _cb('select_responsible:10')))
        _run(_feed(self.dp, self.bot, _cb('final_confirm')))


class FinalConfirmFlowTest(TestCase):
    """AUDIT-10 regression: attachment error must not crash final_confirm."""

    def setUp(self):
        _confirm_locks.clear()
        _reset_router()
        self.dp, self.storage = _make_dp()
        self.bot = _make_bot()
        self.tg_user = TelegramUser.objects.create(
            telegram_id=USER_ID, username='testuser', first_name='Test', last_name='User',
            is_registered=True, bitrix_id=10, bitrix_first_name='Test', bitrix_last_name='User',
        )

    def _setup_confirming(self, responsible_id=10):
        return _run(_set_state(self.storage, TaskState.confirming_tasks, {
            'collected_tasks': [{'title': 'Test task', 'source': 'text'}],
            'list_message_id': 10,
            'responsible_bitrix_id': responsible_id,
            'responsible_name': 'Alice Smith',
        }))

    def _patch_handlers(self, bitrix_result=None, attach_result=True, attach_side_effect=None):
        """Patch all DB and Bitrix calls in final_confirm."""
        mock_user = MagicMock()
        mock_user.bitrix_id = 10
        mock_user.bitrix_first_name = 'Test'
        mock_user.bitrix_last_name = 'User'
        mock_user.telegram_id = USER_ID

        mock_task = MagicMock()
        mock_task.pk = 42
        mock_task.bitrix_task_id = None
        mock_task.bitrix_synced = False

        patches = [
            patch('bot.handlers.tasks.bitrix_service'),
            patch('bot.handlers.tasks.TelegramUser'),
            patch('bot.handlers.tasks.Task'),
            patch('bot.handlers.tasks.sync_to_async'),
        ]
        mocks = [p.start() for p in patches]
        mock_svc, mock_user_model, mock_task_model, mock_sync = mocks

        if attach_side_effect:
            mock_svc.attach_file_to_task = AsyncMock(side_effect=attach_side_effect)
        else:
            mock_svc.attach_file_to_task = AsyncMock(return_value=attach_result)
        mock_svc.create_task = AsyncMock(return_value=bitrix_result or {'ok': True, 'id': '42'})

        mock_user_model.objects.get = MagicMock(return_value=mock_user)
        mock_task_model.objects.bulk_create = MagicMock(return_value=[mock_task])
        mock_task_model.objects.bulk_update = MagicMock()
        mock_task_model.objects.filter = MagicMock()
        mock_task_model.objects.filter.return_value.exists = MagicMock(return_value=False)

        def sync_to_async_side_effect(func):
            async def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        mock_sync.side_effect = sync_to_async_side_effect

        for p in patches:
            self.addCleanup(p.stop)

        return mock_svc, mock_user_model, mock_task_model

    def test_final_confirm_success(self):
        _mock_svc, _mock_user_model, mock_task_model = self._patch_handlers()
        self._setup_confirming()
        _run(_feed(self.dp, self.bot, _cb('final_confirm')))
        mock_task_model.objects.bulk_create.assert_called_once()

    def test_final_confirm_bitrix_error(self):
        _mock_svc, _mock_user_model, mock_task_model = self._patch_handlers(
            bitrix_result={'ok': False, 'error': 'Access denied'}
        )
        self._setup_confirming()
        _run(_feed(self.dp, self.bot, _cb('final_confirm')))
        mock_task_model.objects.bulk_create.assert_called_once()

    def test_final_confirm_attach_exception_no_crash(self):
        """AUDIT-10: str(e) NameError must not crash."""
        _mock_svc, _mock_user_model, mock_task_model = self._patch_handlers(
            attach_side_effect=Exception('Network error')
        )
        self._setup_confirming()
        _run(_feed(self.dp, self.bot, _cb('final_confirm')))
        mock_task_model.objects.bulk_create.assert_called_once()

    def test_final_confirm_idempotency(self):
        _mock_svc, _mock_user_model, mock_task_model = self._patch_handlers()
        self._setup_confirming()
        _run(_feed(self.dp, self.bot, _cb('final_confirm')))
        self.assertEqual(mock_task_model.objects.bulk_create.call_count, 1)
        _run(_feed(self.dp, self.bot, _cb('final_confirm')))
        self.assertEqual(mock_task_model.objects.bulk_create.call_count, 1)


class MediaCollectionFlowTest(TestCase):
    """Album grouping, large file rejection, voice collection."""

    def setUp(self):
        _confirm_locks.clear()
        _reset_router()
        self.dp, self.storage = _make_dp()
        self.bot = _make_bot()
        self.tg_user = TelegramUser.objects.create(telegram_id=USER_ID, is_registered=True)

    def _setup_collecting(self):
        return _run(_set_state(self.storage, TaskState.collecting_tasks, {
            'collected_tasks': [], 'list_message_id': None,
        }))

    def test_photo_collection(self):
        self._setup_collecting()
        _run(_feed(self.dp, self.bot, _photo_msg()))
        data = _run(_get_data(self.storage))
        self.assertEqual(len(data['collected_tasks']), 1)
        self.assertEqual(data['collected_tasks'][0]['source'], 'photo')

    def test_album_grouping(self):
        self._setup_collecting()
        _run(_feed(self.dp, self.bot, _photo_msg(file_id='p1', media_group_id='grp1')))
        _run(_feed(self.dp, self.bot, _photo_msg(file_id='p2', media_group_id='grp1')))
        _run(_feed(self.dp, self.bot, _photo_msg(file_id='p3', media_group_id='grp1')))
        data = _run(_get_data(self.storage))
        tasks = data['collected_tasks']
        self.assertEqual(len(tasks), 1)
        self.assertEqual(len(tasks[0]['files']), 3)

    def test_separate_photos_not_grouped(self):
        self._setup_collecting()
        _run(_feed(self.dp, self.bot, _photo_msg(file_id='p1')))
        _run(_feed(self.dp, self.bot, _photo_msg(file_id='p2')))
        data = _run(_get_data(self.storage))
        self.assertEqual(len(data['collected_tasks']), 2)

    def test_large_file_rejected(self):
        self._setup_collecting()
        _run(_feed(self.dp, self.bot, _voice_msg(file_size=MAX_FILE_SIZE + 1)))
        data = _run(_get_data(self.storage))
        self.assertEqual(len(data['collected_tasks']), 0)

    def test_voice_collection(self):
        self._setup_collecting()
        _run(_feed(self.dp, self.bot, _voice_msg(duration=15)))
        data = _run(_get_data(self.storage))
        task = data['collected_tasks'][0]
        self.assertEqual(task['source'], 'voice')
        self.assertIn('15s', task['title'])

    def test_video_collection(self):
        self._setup_collecting()
        _run(_feed(self.dp, self.bot, _video_msg(duration=60)))
        data = _run(_get_data(self.storage))
        task = data['collected_tasks'][0]
        self.assertEqual(task['source'], 'video')
        self.assertIn('60s', task['title'])

    def test_50_limit_silent(self):
        self._setup_collecting()
        _run(FSMContext(storage=self.storage, key=KEY).update_data(
            collected_tasks=[{'title': f'T{i}', 'source': 'text'} for i in range(50)]
        ))
        _run(_feed(self.dp, self.bot, _msg('Task 51')))
        data = _run(_get_data(self.storage))
        self.assertEqual(len(data['collected_tasks']), 50)


class RegistrationFlowTest(TestCase):
    """Registration: non-numeric bitrix_id, taken bitrix_id."""

    def setUp(self):
        _confirm_locks.clear()
        _reset_router()
        self.dp, self.storage = _make_dp()
        self.bot = _make_bot()
        self.tg_user = TelegramUser.objects.create(
            telegram_id=USER_ID, username='testuser', first_name='Test', last_name='User',
        )

    def test_non_numeric_bitrix_id(self):
        _run(_set_state(self.storage, RegistrationState.waiting_for_bitrix_id))
        _run(_feed(self.dp, self.bot, _msg('abc')))
        state = _run(_get_state(self.storage))
        self.assertEqual(str(state), 'RegistrationState:waiting_for_bitrix_id')

    def test_taken_bitrix_id(self):
        TelegramUser.objects.create(
            telegram_id=222, bitrix_id=42, is_registered=True,
            bitrix_first_name='Other', bitrix_last_name='User',
        )
        _run(_set_state(self.storage, RegistrationState.waiting_for_bitrix_id))
        _run(_feed(self.dp, self.bot, _msg('42')))
        state = _run(_get_state(self.storage))
        self.assertEqual(str(state), 'RegistrationState:waiting_for_bitrix_id')
