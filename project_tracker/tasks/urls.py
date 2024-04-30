from django.urls import path, include
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name = 'index'),
    #path('quality_control/', include('quality_control.urls', namespace='quality_control')),
    # path('another/', views.another_page, name='another_page'),#новый маршрут
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('project/new/', views.create_project, name='create_project'),
]