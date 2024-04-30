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

    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('bugs/<int:bug_id>/update/', views.BugCreateView.as_view(), name='update_bug'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_project'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),

    path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    path('features/<int:feature_id>/update/', views.FeatureCreateView.as_view(), name='update_feature'),
    path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),

]