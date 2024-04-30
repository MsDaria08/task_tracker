from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name = 'index'),
    # # path('bugs/', views.bug_list, name='bug_list'),
    # # path('features/', views.feature_list, name='feature_list'),#новый маршрут
    # # path('bug/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # # path('feature/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    # path('bugs/', views.bug_list, name='bug_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),

    path('', views.index, name = 'index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('bugs/new/', views.create_bug, name='create_bug'),
    path('features/new/', views.create_feature, name='create_feature'),

]