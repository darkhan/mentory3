from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logut, name='logout'),
    path('register/', views.custom_register, name='register'),
]
