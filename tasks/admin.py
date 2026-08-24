from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'telegram_user', 'title', 'status', 'source', 'responsible_name', 'responsible_bitrix_id', 'bitrix_task_id', 'created_at']
    search_fields = ['title', 'telegram_user__username', 'telegram_user__first_name', 'responsible_name']
    list_filter = ['status', 'source', 'created_at']
    ordering = ['-created_at']
    raw_id_fields = ['telegram_user']
