from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect
import re


class DataBase:
    __instance = None
    __connect = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.__instance = None
        self.__connect = None

    def __init__(self, user, psw, port):
        if self.__connect is None:
            self.user = user
            self.psw = psw
            self.port = port
            self.data = "DATA"

    def connect(self):
        print(f"Соединение с Базой данных:{self.user}, "
              f"{self.psw}, {self.port}")

    def close(self):
        print("Закрыть соединение с Базой данных")

    def read(self):
        return "Данные из Базы данных"

    def write(self):
        print(f"Запись в Базу данных {self.data}")


def index(request):
    return render(request, 'people/index.html')


pri_info = {
    'abramov': ['Абрамов Александр Альбертович', '22-2.034'],
    'bliznuk': ['Близнюк Илья Сергеевич', '22-2.035'],
    'zverev': ['Зверев Андрей Александрович', '22-2.036'],
    'karaguzin': ['Карагузин Максим Игоревич', '22-2.037'],
    'kruglik': ['Круглик Евгений Дмитриевич', '22-2.038'],
    'luskov': ['Лысков Влас Евгеньевич', '22-2.039'],
    'maklyusov': ['Маклюсов Роман Романович', '21-2.010'],
    'maneshin': ['Манешин Антон Сергеевич', '22-2.040'],
    'petrachkov': ['Петрачков Александр Викторович', '22-2.041'],
    'safonov': ['Сафонов Глеб Александрович', '22-2.045'],
    'tereshin': ['Терешин Роман Павлович 🎶(❁´◡`❁)', '22-2.042'],
    'chertcov': ['Чертков Федор Андреевич', '22-2.043'],
}


def pri_group(request):
    out = '<h1> ПрИ-201 </h1> <p>'
    for number, mas_of_info in pri_info.items():
        out += number + '.'
        out += mas_of_info[0]
        out += '</p>'
    return render(request, 'people/pri_group.html', context=pri_info)


def pri_id(request, number_student):
    try:
        out = '<h1> ПрИ-201 </h1> <p>'
        buff = 0
        for key, item in pri_info.items():
            buff += 1
            if buff == number_student:
                out += item[0] + ' ' + item[1]
                break
        out += '</p>'
        return HttpResponse(out)
    except:
        out = '<h1> Ошибка </h1> <h3> Такого студента не существует </h3>'
        return HttpResponse(out)


dict_object_types = {
    'int': '1',
    'float': 1.1,
    'str': 'some_string',
    'list': [1, 2, 3],
    'dict': {'key': 'value'},
    'tuple': [4, 5, 6],
    'set': {'seven', 'eight'},
    'bool': True,
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
            return HttpResponse(f'<h1>{new_ml}</h1>')
        buff = i + 1

    if line[buff:len(line)] not in new_ml:
        new_ml.append(line[buff:len(line)])

    for i in new_ml:
        if i == '':
            new_ml.pop(new_ml.index(i))

    for i in range(len(new_ml)):
        k = new_ml[i].count('"')
        if k > 1 and k % 2 == 0:
            new_ml[i] = new_ml[i].replace('"', '')
        elif k > 1 and k % 2 != 0:
            new_ml[i] = new_ml[i].replace('"', '', k - 1)

    return HttpResponse(f'<h1>{new_ml}</h1>')


def redirect_to_home(request):
    return redirect(index)


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
