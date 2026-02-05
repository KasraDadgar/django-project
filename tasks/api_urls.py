from django.urls import path
from .views import TaskListCreateAPI, TaskDetailAPI

app_name = 'tasks_api'

urlpatterns = [
    path('tasks/', TaskListCreateAPI.as_view(), name='task_list_create_api'),
    path('tasks/<int:pk>/', TaskDetailAPI.as_view(), name='task_detail_api'),
]
