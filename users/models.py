from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True, verbose_name='Telegram ID')
    username = models.CharField(max_length=255, blank=True, null=True, verbose_name='Username')
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last Name')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone Number')
    bitrix_id = models.IntegerField(null=True, blank=True, unique=True, verbose_name='Bitrix ID')
    bitrix_first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Bitrix First Name')
    bitrix_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Bitrix Last Name')
    is_registered = models.BooleanField(default=False, verbose_name='Registered')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username or self.first_name or self.telegram_id}"
