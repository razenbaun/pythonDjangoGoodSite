from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AddPortfolioForm(forms.Form):
    slug = forms.SlugField(max_length=255)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    skills = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 10}))
    photo_1 = forms.ImageField(required=False)
    link_1 = forms.URLField(required=False)
    photo_2 = forms.ImageField(required=False)
    link_2 = forms.URLField(required=False)
    photo_3 = forms.ImageField(required=False)
    link_3 = forms.URLField(required=False)
    photo_4 = forms.ImageField(required=False)
    link_4 = forms.URLField(required=False)
    photo_5 = forms.ImageField(required=False)
    link_5 = forms.URLField(required=False)
    photo_6 = forms.ImageField(required=False)
    link_6 = forms.URLField(required=False)
    photo_7 = forms.ImageField(required=False)
    link_7 = forms.URLField(required=False)
    photo_8 = forms.ImageField(required=False)
    link_8 = forms.URLField(required=False)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
