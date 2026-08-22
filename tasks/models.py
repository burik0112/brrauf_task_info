from django.db import models
from users.models import TelegramUser


class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    class Source(models.TextChoices):
        TEXT = 'text', 'Text'
        VOICE = 'voice', 'Voice'
        VIDEO = 'video', 'Video'
        PHOTO = 'photo', 'Photo'
        VIDEO_NOTE = 'video_note', 'Video Note'

    telegram_user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    title = models.CharField(max_length=500)
    responsible_bitrix_id = models.IntegerField(null=True, blank=True, verbose_name='Responsible Bitrix ID')
    responsible_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Responsible Name')
    bitrix_task_id = models.IntegerField(null=True, blank=True, verbose_name='Bitrix Task ID')
    bitrix_synced = models.BooleanField(default=False, verbose_name='Bitrix Synced')
    bitrix_error = models.CharField(max_length=500, blank=True, default='', verbose_name='Bitrix Error')
    telegram_file_id = models.TextField(blank=True, default='', verbose_name='Telegram File ID')
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    source = models.CharField(
        max_length=10,
        choices=Source.choices,
        default=Source.TEXT,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title[:50]
