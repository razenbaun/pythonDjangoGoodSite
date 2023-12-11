from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from people.forms import RegisterUserForm

menu = [
    {'title': 'О сайте', 'url_n': 'about'},
    {'title': 'Группа ПрИ-201', 'url_n': 'pri_group'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context


def index(request):
    data = {
        'menu': menu,
        'title': "Главная страница"
    }
    return render(request, 'people/index.html', context=data)


pri = {
    '1': 'Абрамов Александр Альбертович, 22-2.034',
    '2': 'Близнюк Илья Сергеевич, 22-2.035',
    '3': 'Зверев Андрей Александрович, 22-2.036',
    '4': 'Карагузин Максим Игоревич, 22-2.037',
    '5': 'Круглик Евгений Дмитриевич, 22-2.038',
    '6': 'Лысков Влас Евгеньевич, 22-2.039',
    '7': 'Маклюсов Роман Романович, 21-2.010',
    '8': 'Манешин Антон Сергеевич, 22-2.040',
    '9': 'Петрачков Александр Викторович, 22-2.041',
    '10': 'Сафонов Глеб Александрович, 22-2.045',
    '11': 'Терешин Роман Павлович, 22-2.042',
    '12': 'Чертков Федор Андреевич, 22-2.043',
}


def pri_group(request):
    data = {
        'menu': menu,
        'title': "ПрИ-201",
        'pri': pri,
    }
    return render(request, 'people/pri_group.html', context=data)


def pri_id(request, number_student):
    data = {
        'menu': menu,
        'title': pri.get(str(number_student)),
        'student': 'image/' + str(number_student) + '.jpg',
    }
    return render(request, 'people/pri_id.html', context=data)


def about(request):
    data = {
        'menu': menu,
        'title': "О сайте",
    }
    return render(request, 'people/about.html', context=data)


def redirect_to_home(request):
    return redirect(index)


def categories(request):
    return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')


def server_down(exception):
    return HttpResponseServerError('<h1> Сервер упал! Страница недоступна <h1>')


def forbidden(request, exception):
    return HttpResponseForbidden('<h1> Доступ запрещён! <h1>')


def bad_request(request, exception):
    return HttpResponseBadRequest('<h1> Запрос ошибочен! <h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес!!! </h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'people/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
