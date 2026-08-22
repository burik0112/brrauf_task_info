from django.test import TestCase, Client
from django.contrib.auth.models import User
from unittest.mock import patch, AsyncMock, MagicMock
import json

from tasks.models import Task
from users.models import TelegramUser
from bot.handlers.tasks import (
    format_collected_tasks,
    format_task_for_confirm,
    MAX_COLLECTED_TASKS,
    MAX_TITLE_LENGTH,
    TELEGRAM_MAX_TEXT,
)


class FormatCollectedTasksTest(TestCase):
    def test_empty_tasks(self):
        result = format_collected_tasks([])
        self.assertEqual(result, "📭 Vazifalar yo'q.")

    def test_single_task(self):
        tasks = [{'title': 'Test task', 'source': 'text'}]
        result = format_collected_tasks(tasks)
        self.assertIn('1. 📝 Test task', result)
        self.assertIn('1 ta', result)

    def test_multiple_tasks(self):
        tasks = [
            {'title': 'Task 1', 'source': 'text'},
            {'title': 'Task 2', 'source': 'voice'},
            {'title': 'Task 3', 'source': 'photo'},
        ]
        result = format_collected_tasks(tasks)
        self.assertIn('1. 📝 Task 1', result)
        self.assertIn('2. 🎤 Task 2', result)
        self.assertIn('3. 🖼 Task 3', result)
        self.assertIn('3 ta', result)

    def test_html_escaping(self):
        tasks = [{'title': '<script>alert("xss")</script>', 'source': 'text'}]
        result = format_collected_tasks(tasks)
        self.assertNotIn('<script>', result)
        self.assertIn('&lt;script&gt;', result)

    def test_html_escaping_ampersand(self):
        tasks = [{'title': 'A & B < C', 'source': 'text'}]
        result = format_collected_tasks(tasks)
        self.assertIn('A &amp; B &lt; C', result)

    def test_title_truncation(self):
        long_title = 'x' * (MAX_TITLE_LENGTH + 100)
        tasks = [{'title': long_title, 'source': 'text'}]
        result = format_collected_tasks(tasks)
        self.assertIn('x' * MAX_TITLE_LENGTH, result)
        self.assertNotIn('x' * (MAX_TITLE_LENGTH + 1), result)

    def test_max_tasks_warning(self):
        tasks = [{'title': f'Task {i}', 'source': 'text'} for i in range(MAX_COLLECTED_TASKS)]
        result = format_collected_tasks(tasks)
        self.assertIn(f'Maksimal {MAX_COLLECTED_TASKS} ta vazifa', result)

    def test_result_within_telegram_limit(self):
        tasks = [{'title': 'x' * 50, 'source': 'text'} for i in range(20)]
        result = format_collected_tasks(tasks)
        self.assertLessEqual(len(result), TELEGRAM_MAX_TEXT)

    def test_emoji_numbering_10_plus(self):
        tasks = [{'title': f'Task {i}', 'source': 'text'} for i in range(15)]
        result = format_collected_tasks(tasks)
        self.assertIn('10. ', result)
        self.assertIn('11. ', result)
        self.assertIn('15. ', result)
        self.assertNotIn('10️⃣', result)


class FormatTaskForConfirmTest(TestCase):
    def test_basic_format(self):
        tasks = [{'title': 'Task 1', 'source': 'text'}]
        result = format_task_for_confirm(tasks, 'John Doe')
        self.assertIn('John Doe', result)
        self.assertIn('Task 1', result)
        self.assertIn('Tasdiqlaysizmi?', result)

    def test_html_escaping_in_responsible_name(self):
        tasks = [{'title': 'Task', 'source': 'text'}]
        result = format_task_for_confirm(tasks, '<b>Test</b>')
        self.assertIn('&lt;b&gt;Test&lt;/b&gt;', result)

    def test_html_escaping_in_task_title(self):
        tasks = [{'title': 'A & B', 'source': 'text'}]
        result = format_task_for_confirm(tasks, 'User')
        self.assertIn('A &amp; B', result)


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = TelegramUser.objects.create(
            telegram_id=123456789,
            username='testuser',
            first_name='Test',
            last_name='User',
            is_registered=True,
        )

    def test_create_task(self):
        task = Task.objects.create(
            telegram_user=self.user,
            title='Test task',
            status=Task.Status.PENDING,
            source=Task.Source.TEXT,
        )
        self.assertEqual(task.title, 'Test task')
        self.assertEqual(task.status, Task.Status.PENDING)
        self.assertFalse(task.bitrix_synced)
        self.assertEqual(task.bitrix_error, '')
        self.assertEqual(task.telegram_file_id, '')

    def test_task_str(self):
        task = Task.objects.create(
            telegram_user=self.user,
            title='x' * 100,
        )
        self.assertEqual(str(task), 'x' * 50)

    def test_task_status_choices(self):
        self.assertEqual(Task.Status.PENDING, 'pending')
        self.assertEqual(Task.Status.COMPLETED, 'completed')
        self.assertEqual(Task.Status.CANCELLED, 'cancelled')

    def test_task_source_choices(self):
        self.assertEqual(Task.Source.TEXT, 'text')
        self.assertEqual(Task.Source.VOICE, 'voice')
        self.assertEqual(Task.Source.VIDEO, 'video')
        self.assertEqual(Task.Source.PHOTO, 'photo')
        self.assertEqual(Task.Source.VIDEO_NOTE, 'video_note')


class TelegramUserModelTest(TestCase):
    def test_create_user(self):
        user = TelegramUser.objects.create(
            telegram_id=987654321,
            username='newuser',
            first_name='New',
            last_name='User',
        )
        self.assertEqual(user.telegram_id, 987654321)
        self.assertFalse(user.is_registered)

    def test_user_str(self):
        user = TelegramUser.objects.create(
            telegram_id=111222333,
            first_name='Alice',
        )
        self.assertEqual(str(user), 'Alice')

    def test_user_str_fallback_to_username(self):
        user = TelegramUser.objects.create(
            telegram_id=444555666,
            username='bob',
        )
        self.assertEqual(str(user), 'bob')

    def test_user_str_fallback_to_telegram_id(self):
        user = TelegramUser.objects.create(
            telegram_id=777888999,
        )
        self.assertEqual(str(user), '777888999')

    def test_unique_bitrix_id(self):
        TelegramUser.objects.create(
            telegram_id=111,
            bitrix_id=42,
        )
        with self.assertRaises(Exception):
            TelegramUser.objects.create(
                telegram_id=222,
                bitrix_id=42,
            )


class HealthCheckTest(TestCase):
    def test_health_endpoint(self):
        client = Client()
        response = client.get('/health/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'ok')


class RecentIdsQueryTest(TestCase):
    def setUp(self):
        self.user = TelegramUser.objects.create(
            telegram_id=123456789,
            is_registered=True,
        )

    def test_recent_ids_deduplication(self):
        for _ in range(5):
            Task.objects.create(
                telegram_user=self.user,
                title='Task',
                responsible_bitrix_id=42,
            )
        Task.objects.create(
            telegram_user=self.user,
            title='Task',
            responsible_bitrix_id=99,
        )
        ids = list(Task.objects.filter(
            telegram_user=self.user
        ).exclude(
            responsible_bitrix_id__isnull=True
        ).order_by('-created_at').values_list('responsible_bitrix_id', flat=True)[:50])
        unique_ids = list(dict.fromkeys(ids))[:5]
        self.assertEqual(len(unique_ids), 2)
        self.assertIn(99, unique_ids)
        self.assertIn(42, unique_ids)
        self.assertEqual(unique_ids[0], 99)
