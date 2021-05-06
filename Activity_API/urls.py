from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.Index, name= 'index'),
    path('', views.MyAPI, name= 'api'),
    path('all_task/', views.MyTaskList, name= 'all_activity'),
    path('detail/<str:pk>/', views.MyTaskDetail, name= 'activity by id'),
    path('update/<str:pk>/', views.MyTaskUpdate, name= 'update activity'),
    path('create/', views.MyTaskCreate, name = "create new activity"),
    path('delete/<str:pk>/', views.MyTaskDelete, name = 'activity delete')
]