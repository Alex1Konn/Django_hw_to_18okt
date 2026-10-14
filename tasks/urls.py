from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.index),
    path('task_2', views.task_2),
    path('task_3', views.task_3),
    path('task_4', views.task_4),
    path('task_5', views.task_5),
    path('task_6', views.task_6),
    path('task_7', views.task_7),
    path('task_8', views.task_8),
    path('task_9', views.task_9),
    path('task_10', views.task_10),
    path('employee_list', views.employee_list),
    path('default_employees', views.default_employees),
    ]