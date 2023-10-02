from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


class DateProcessing():
    def archive(request, year):
        return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")


pri_info = {
    '1': ['Абрамов Александр Альбертович', '22-2.034'],
    '2': ['Близнюк Илья Сергеевич', '22-2.035'],
    '3': ['Зверев Андрей Александрович', '22-2.036'],
    '4': ['Карагузин Максим Игоревич', '22-2.037'],
    '5': ['Круглик Евгений Дмитриевич', '22-2.038'],
    '6': ['Лысков Влас Евгеньевич', '22-2.039'],
    '7': ['Маклюсов Роман Романович', '21-2.010'],
    '8': ['Манешин Антон Сергеевич', '22-2.040'],
    '9': ['Петрачков Александр Викторович', '22-2.041'],
    '10': ['Сафонов Глеб Александрович', '22-2.045'],
    '11': ['Терешин Роман Павлович 🎶(❁´◡`❁)', '22-2.042'],
    '12': ['Чертков Федор Андреевич', '22-2.043'],
}


# Create your views here.

def index(request):
    out = dict(request.GET)
    out = out.values()
    return HttpResponse(f"Страница для Людей")


def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')


def pri_group(request):
    out = '<h1> ПрИ-201 </h1> <p>'
    for number, mas_of_info in pri_info.items():
        out += number + '.'
        out += mas_of_info[0]
        out += '</p>'

    return HttpResponse(out)


def pri_id(request, number_student):
    if str(number_student) in pri_info:
        out = '<h1> ПрИ-201 </h1> <p>'
        mas_of_info = pri_info[str(number_student)]
        for info in mas_of_info:
            out += info + ' '
        out += '</p>'
        return HttpResponse(out)
    else:
        out = '<h1> Ошибка </h1> <h3> Такого студента не существует </h3>'
        return HttpResponse(out)


def categories(request, cat):
    return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес!!! </h1>')


def server_down(request):
    return HttpResponseNotFound('<h1> Проблема на стороне сервера!!! </h1>')


def access_is_denied(request, exception):
    return HttpResponseNotFound('<h1> Доступ запрещён!!! </h1>')


def request_cannot_be_processed(request, exception):
    return HttpResponseNotFound('<h1> Невозможно обработать запрос!!! </h1>')
