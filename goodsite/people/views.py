from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from people.forms import RegisterUserForm, LoginUserForm
from .models import *

menu = [
    {'title': 'Портфолио', 'url_n': 'portfolio'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'people/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'people/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
    data = {
        'menu': menu,
    }
    return render(request, 'people/index.html', context=data)


def portfolio(request):
    posts = Portfolio.objects.all()
    data = {
        'menu': menu,
        'title': 'Портфолио',
        'posts': posts
    }
    return render(request, 'people/portfolio.html', context=data)


def show_portfolio(request, portfolio_id):
    return HttpResponse(f"Отображение Портфолио с id = {portfolio_id}")


def redirect_to_home(request):
    return redirect(index)


def profile(request):
    data = {
        'menu': menu,
        'title': "Ваше портфолио",
    }
    if request.user.is_authenticated:
        return render(request, 'people/profile.html', context=data)
    else:
        return redirect('login')


def categories(request, cat):
    return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')


def server_down(exception):
    return HttpResponseServerError('<h1> Сервер упал! Страница недоступна <h1>')


def forbidden(request, exception):
    return HttpResponseForbidden('<h1> Доступ запрещён! <h1>')


def bad_request(request, exception):
    return HttpResponseBadRequest('<h1> Запрос ошибочен! <h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес!!! </h1>')


