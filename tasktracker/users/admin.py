from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm, ChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = ChangeForm
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
