from django.urls import path
from django.contrib import admin
from . import views
from tasks import views as tasks_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', tasks_views.signup, name='signup'),
    path('signout/', tasks_views.signout, name='signout'),
    path('signin/', tasks_views.signin, name='signin'),
    path('tasks/', tasks_views.tasks, name='tasks'),
    path('tasks/pending/', tasks_views.tasks_pending, name='tasks_pending'),
    path('tasks/finish/', tasks_views.tasks_finish, name='tasks_finish'),
    path('tasks/create', tasks_views.tasks_create, name='tasks_create'),
    path('tasks/edit/<int:task_id>/', tasks_views.tasks_edit, name='tasks_edit'),
    path('tasks/search/', tasks_views.tasks_search, name='tasks_search'),
    path('tasks/anonymous/', tasks_views.public_tasks, name='anonymous_tasks'),
    path('tasks/complete/<int:task_id>/', tasks_views.task_complete, name='tasks_complete'),
    path('tasks/delete/<int:task_id>/', tasks_views.task_delete, name='tasks_delete'),
]
