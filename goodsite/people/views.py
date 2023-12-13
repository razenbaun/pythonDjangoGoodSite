from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from people.forms import RegisterUserForm, LoginUserForm, AddPortfolioForm
from .models import *
from django.http import Http404

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


def show_portfolio(request, portfolio_slug):
    post = get_object_or_404(Portfolio, slug=portfolio_slug)

    data = {
        'post': post,
        'menu': menu,
        'title': 'Портфолио'
    }

    return render(request, 'people/portfolio_id.html', context=data)


def add_portfolio(request):
    if request.method == 'POST':
        form = AddPortfolioForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = AddPortfolioForm(user=request.user)
    data = {
        'form': form,
        'menu': menu,
        'title': 'Добавить Портфолио'
    }
    return render(request, 'people/add_portfolio.html', context=data)


def profile(request):
    if request.user.is_authenticated:
        try:
            post = get_object_or_404(Portfolio, user=request.user)
        except Http404:
            return redirect('add_portfolio')
        data = {
            'post': post,
            'menu': menu,
            'title': "Ваше портфолио",
        }
        return render(request, 'people/profile.html', context=data)
    else:
        return redirect('login')


def delete_portfolio(request):
    portfolio = get_object_or_404(Portfolio, user=request.user)

    if request.method == 'POST':
        portfolio.delete()
        return redirect('profile')

    data = {
        'portfolio': portfolio,
        'menu': menu,
    }
    return render(request, 'delete_portfolio.html', context=data)


def edit_portfolio(request):
    portfolio = get_object_or_404(Portfolio, user=request.user)

    if request.method == 'POST':
        # Обработка данных, отправленных пользователем при редактировании
        form = AddPortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            # Обработка успешного изменения, например, перенаправление на другую страницу
            return redirect('portfolio_list')
    else:
        form = AddPortfolioForm(instance=portfolio)

    return render(request, 'edit_portfolio.html', {'form': form, 'portfolio': portfolio})


def redirect_to_home(request):
    return redirect(index)


def server_down(exception):
    return HttpResponseServerError('<h1> Сервер упал! Страница недоступна <h1>')


def forbidden(request, exception):
    return HttpResponseForbidden('<h1> Доступ запрещён! <h1>')


def bad_request(request, exception):
    return HttpResponseBadRequest('<h1> Запрос ошибочен! <h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес!!! </h1>')
