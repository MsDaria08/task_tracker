from django.urls import path, include
from tasks import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index),
    path('quality_control/', include('quality_control.urls', namespace='quality_control')),
    path('another/', views.another_page, name='another_page'),#новый маршрут
]