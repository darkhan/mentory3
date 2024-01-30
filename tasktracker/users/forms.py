from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
