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


class TaskSearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100, required=False)
    completed_choices = (
        ("", "All tasks"),
        ("0", "Pending"),
        ("1", "Completed"),
    )
    completed = forms.ChoiceField(choices=completed_choices, required=False)

