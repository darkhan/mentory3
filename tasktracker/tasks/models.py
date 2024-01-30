# models.py
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_time = models.DateTimeField()
    due_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
