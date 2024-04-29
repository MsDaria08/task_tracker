from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_url = reverse('quality_control:index')
    html = (f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на другую страницы</a>"
            f"<br>Для перехода на главную страницу quality_control перейдите <a href='{quality_control_url}'>сюда</a>")
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Эта другая страница приложения tasks")
