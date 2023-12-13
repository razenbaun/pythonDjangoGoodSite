from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AddPortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['slug', 'description', 'skills', 'photo_1', 'link_1', 'photo_2', 'link_2', 'photo_3', 'link_3',
                  'photo_4', 'link_4', 'photo_5', 'link_5', 'photo_6', 'link_6', 'photo_7', 'link_7', 'photo_8',
                  'link_8']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # Получить пользователя из аргументов и удалить его
        super(AddPortfolioForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        portfolio = super(AddPortfolioForm, self).save(commit=False)
        portfolio.user = self.user  # Установить пользователя в поле "user"
        if commit:
            portfolio.save()
        return portfolio


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
