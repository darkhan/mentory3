# catalog/admin.py
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'description', 'created_time', 'due_time', 'completed')
    search_fields = ('name', 'user', 'completed')


admin.site.register(Task, TaskAdmin)

