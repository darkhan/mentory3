# views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Task
from .forms import TaskForm, TaskSearchForm
from django.contrib.postgres.search import SearchVector

from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_queryset(self):
        base_qs = super(TaskDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        searchable_fields = ["name", "description"]
        filter_conditions = {
            'user': self.request.user
        }

        query = self.request.GET.get("q")
        if query:
            filter_conditions['search'] = query

        query_completed = self.request.GET.get("completed")
        if query_completed:
            filter_conditions['completed'] = query_completed

        return Task.objects.annotate(search=SearchVector(*searchable_fields)).filter(**filter_conditions)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = TaskSearchForm(self.request.GET)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    # todo: check due date if not today
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was updated successfully.")
        return super().form_valid(form)

    def get_queryset(self):
        base_qs = super(TaskUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'The task was deleted successfully.')
        return response

    def get_queryset(self):
        base_qs = super(TaskDeleteView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TasksViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, ) # (IsAuthenticatedOrReadOnly, ) # IsAdminOnly

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Task.objects.filter(user=self.request.user)

        return Task.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    # categoreis
    def completed(self, request):
        completed_choices = (
            ("", "All tasks"),
            ("0", "Pending"),
            ("1", "Completed"),
        )
        return Response({'cats': completed_choices})
