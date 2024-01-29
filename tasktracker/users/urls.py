from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logut, name='custom_logout'),
    path('register/', views.custom_register, name='custom_register'),
]
