from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logut, name='custom_logout'),
]
