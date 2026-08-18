from django.contrib import admin
from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = [
        'telegram_id', 'username', 'first_name', 'last_name',
        'phone_number', 'bitrix_id', 'is_registered', 'created_at',
    ]
    search_fields = ['telegram_id', 'username', 'first_name', 'last_name', 'phone_number', 'bitrix_id']
    list_filter = ['is_registered', 'created_at']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['telegram_id', 'created_at', 'updated_at']
        return ['created_at', 'updated_at']
