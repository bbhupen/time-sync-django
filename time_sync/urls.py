from django.urls import path
app_name = 'time_sync'
from . import views

urlpatterns = [
    path('', views.register),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout')
]