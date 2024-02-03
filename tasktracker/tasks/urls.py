# urls.py

from django.urls import path
from .views import TasksListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetail, TasksViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('tasks/', TasksListView.as_view(), name='task_list'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>', TaskDetail.as_view(), name='task'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
]

router = SimpleRouter()
router.register('api/v1/tasks', TasksViewSet, basename='tasks')

urlpatterns += router.urls
