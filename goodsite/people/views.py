from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect
import re

menu = [
    {'title': 'Главная', 'url_n': 'home'},
    {'title': ' О сайте', 'url_n': 'about'}
]


def index(request):
    data = {
        'menu': menu,
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

pri_info = {'pri': pri}


def pri_group(request):
    return render(request, 'people/pri_group.html', context=pri_info)


def pri_id(request, number_student):
    try:
        out = '<h1> ПрИ-201 </h1> <p>'
        buff = 0
        for key, item in pri.items():
            if key == str(number_student):
                out += item
                break
        out += '</p>'
        return HttpResponse(out)
    except:
        out = '<h1> Ошибка </h1> <h3> Такого студента не существует </h3>'
        return HttpResponse(out)


dict_object_types = {
    'bool': False,
    'int': 1886,
    'float': 3.14,
    'str': 'string',
    'tuple': [4, 5, 6],
    'set': {'item_one', 'item_two'},
    'list': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    'dict': {'key': 'value'},
    'test_str': 'Hello, world!',
}


def object_types(request):
    return render(request, 'people/object_types.html', context=dict_object_types)


def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')


def post_detail(request):
    if request.GET:
        s = ''.join([f'{key}={value[0]}|' for key, value in dict(request.GET).items()])[:-1]
        return HttpResponse(f'<h1>{s}</h1>')
    else:
        return HttpResponse(f'<h1>Get is empty</h1>')


def split_line(request, line, sepp):
    flag = True
    ml = []
    new_ml = []

    for i in range(len(line)):
        if line[i] == '"' and flag:
            flag = False
        elif line[i] == '"' and not flag:
            flag = True
        elif line[i] != '"' and sepp == line[i] and flag:
            ml.append(i)

    buff = 0
    for i in ml:
        new_ml.append(line[buff:i])
        if buff + 1 > len(line):
            break
        buff = i + 1

    if line[buff:len(line)] not in new_ml:
        new_ml.append(line[buff:len(line)])

    for i in range(len(new_ml)):
        k = new_ml[i].count('"')
        if k > 1 and k % 2 == 0:
            new_ml[i] = new_ml[i].replace('"', '')
        elif k > 1 and k % 2 != 0:
            new_ml[i] = new_ml[i].replace('"', '', k - 1)

    for i in new_ml:
        if i == '':
            new_ml.pop(new_ml.index(i))

    return HttpResponse(f'<h1>{new_ml}</h1>')


def redirect_to_home(request):
    return redirect(index)


value = 'capfirst'


def filters(request):
    return render(request, 'people/filters.html', context=dict_object_types)


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
