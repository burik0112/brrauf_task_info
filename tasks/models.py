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

    telegram_user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    title = models.CharField(max_length=500)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title[:50]
