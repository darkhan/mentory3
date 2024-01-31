# forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_time', 'completed']
        widgets = {
            'due_time': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
