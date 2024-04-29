from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bug_list = reverse('quality_control:bug_list')
    feature_list = reverse('quality_control:feature_list')
    html = (f"<h1>Страница контроля качества </h1><a href='{bug_list}'> <br> Список всех багов</a>"
            f"<br><a href='{feature_list}'> Запросы на улучшение</a>")
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
