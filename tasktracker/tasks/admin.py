# catalog/admin.py
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_time', 'end_time')
    search_fields = ('name', 'user')


admin.site.register(Task, TaskAdmin)

