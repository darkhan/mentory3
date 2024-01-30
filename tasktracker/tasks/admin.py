# catalog/admin.py
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_time', 'due_time')
    search_fields = ('name', 'user')


admin.site.register(Task, TaskAdmin)

