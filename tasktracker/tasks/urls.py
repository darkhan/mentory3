# urls.py

from django.urls import path
from .views import TasksListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('tasks/', TasksListView.as_view(), name='task_list'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
]
