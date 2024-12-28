from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks, name='tasks'),
    path('pending/', tasks_pending, name='tasks_pending'),
    path('finish/', tasks_finish, name='tasks_finish'),
    path('create', tasks_create, name='tasks_create'),
    path('edit/<int:task_id>/', tasks_edit, name='tasks_edit'),
    path('search/', tasks_search, name='tasks_search'),
    path('anonymous/', public_tasks, name='anonymous_tasks'),
    path('complete/<int:task_id>/', task_complete, name='tasks_complete'),
    path('delete/<int:task_id>/', task_delete, name='tasks_delete'),
]