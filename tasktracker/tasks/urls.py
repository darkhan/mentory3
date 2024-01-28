# urls.py

from django.urls import path
from .views import TasksListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('tasks/', TasksListView.as_view(), name='task_list'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
]
