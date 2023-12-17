from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from people.forms import RegisterUserForm, LoginUserForm, AddPortfolioForm, AcademicAchievementsForm
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


def privacy(request):
    data = {
        'menu': menu,
    }
    return render(request, 'people/privacy.html', context=data)


def portfolio(request):
    posts = Portfolio.objects.all()
    data = {
        'menu': menu,
        'title': 'Портфолио',
        'posts': posts
    }
    return render(request, 'people/portfolio.html', context=data)


def show_portfolio(request, portfolio_slug):
    portfolio = get_object_or_404(Portfolio, slug=portfolio_slug)
    academic_achievements = AcademicAchievements.objects.filter(user=portfolio.user)

    data = {
        'show_academic_achievements': 'portfolio/' + str(portfolio_slug) + '/academic-achievements',
        'show_creative_achievements': 'portfolio/' + str(portfolio_slug) + '/creative-achievements',
        'show_sport_achievements': 'portfolio/' + str(portfolio_slug) + '/sport-achievements',
        'show_social_activity': 'portfolio/' + str(portfolio_slug) + '/social-activity  ',
        'show_personal_achievements': 'portfolio/' + str(portfolio_slug) + '/personal-achievements',
        'portfolio': portfolio,
        'menu': menu,
        'title': 'Портфолио',
        'academic_achievements': academic_achievements
    }

    return render(request, 'people/portfolio_id.html', context=data)


def portfolio_cat(request, portfolio_slug, cat_slug):
    portfolio = get_object_or_404(Portfolio, slug=portfolio_slug)

    category = get_object_or_404(Category, slug=cat_slug)

    academic_achievements = AcademicAchievements.objects.filter(user=portfolio.user, cat=category)

    data = {
        'show_academic_achievements': 'portfolio/' + str(portfolio_slug) + '/academic-achievements',
        'show_creative_achievements': 'portfolio/' + str(portfolio_slug) + '/creative-achievements',
        'show_sport_achievements': 'portfolio/' + str(portfolio_slug) + '/sport-achievements',
        'show_social_activity': 'portfolio/' + str(portfolio_slug) + '/social-activity  ',
        'show_personal_achievements': 'portfolio/' + str(portfolio_slug) + '/personal-achievements',
        'portfolio': portfolio,
        'menu': menu,
        'title': 'Портфолио',
        'academic_achievements': academic_achievements
    }

    return render(request, 'people/portfolio_id.html', context=data)


def delete_portfolio(request):
    portfolio = get_object_or_404(Portfolio, user=request.user)

    if request.method == 'POST':
        portfolio.delete()
        return redirect('profile')

    data = {
        'portfolio': portfolio,
        'menu': menu,
    }
    return render(request, 'people/profile.html', context=data)


def profile(request):
    if request.user.is_authenticated:
        try:
            portfolio = get_object_or_404(Portfolio, user=request.user)
            academic_achievements = AcademicAchievements.objects.filter(user=portfolio.user)
        except Http404:
            return redirect('add_portfolio')
        data = {
            'show_academic_achievements': 'profile/academic-achievements',
            'show_creative_achievements': 'profile/creative-achievements',
            'show_sport_achievements': 'profile/sport-achievements',
            'show_social_activity': 'profile/social-activity  ',
            'show_personal_achievements': 'profile/personal-achievements',
            'portfolio': portfolio,
            'menu': menu,
            'title': 'Ваше Портфолио',
            'academic_achievements': academic_achievements
        }
        return render(request, 'people/profile.html', context=data)
    else:
        return redirect('login')


def profile_cat(request, cat_slug):
    if request.user.is_authenticated:
        try:
            category = get_object_or_404(Category, slug=cat_slug)
            portfolio = get_object_or_404(Portfolio, user=request.user)
            academic_achievements = AcademicAchievements.objects.filter(user=portfolio.user, cat=category)
        except Http404:
            return redirect('add_portfolio')
        data = {
            'show_academic_achievements': 'profile/academic-achievements',
            'show_creative_achievements': 'profile/creative-achievements',
            'show_sport_achievements': 'profile/sport-achievements',
            'show_social_activity': 'profile/social-activity  ',
            'show_personal_achievements': 'profile/personal-achievements',
            'portfolio': portfolio,
            'menu': menu,
            'title': 'Ваше Портфолио',
            'academic_achievements': academic_achievements
        }
        return render(request, 'people/profile_cat.html', context=data)
    else:
        return redirect('login')


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


def add_academic(request):
    if request.method == 'POST':
        form = AcademicAchievementsForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AcademicAchievementsForm(user=request.user)
    data = {
        'form': form,
        'menu': menu,
        'title': 'Добавить Достижение'
    }
    return render(request, 'people/add_academic.html', context=data)


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
