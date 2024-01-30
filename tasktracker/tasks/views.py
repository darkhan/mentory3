# views.py

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Task
from django.urls import reverse_lazy


class TasksListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['name', 'description', 'start_time', 'due_time', 'user']


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['name', 'description', 'created_time', 'due_time', 'user']
    success_url = reverse_lazy('project-list')
