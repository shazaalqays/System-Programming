from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home),
    path('', auth_views.LoginView.as_view(template_name='accounts/LOGIN.html')),
]
