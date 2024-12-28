from django.urls import path, include
from django.contrib import admin
from . import views
from tasks import views as tasks_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', tasks_views.signup, name='signup'),
    path('signout/', tasks_views.signout, name='signout'),
    path('signin/', tasks_views.signin, name='signin'),
    path('tasks/', include('tasks.urls'), name='tasks'),
]
