from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(f"<h1>Текущее время: {msg}</h1><br><a href={reverse('home')}>Home</a>")


def workdir_view(request):
    path = f'./'
    files = listdir(path=path)
    return HttpResponse(f"<h1>Список файлов в директории:</h1><br>{files}<br><a href={reverse('home')}>Home</a>")

