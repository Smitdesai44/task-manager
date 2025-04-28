
from django.urls import path
from .views import *

urlpatterns = [
    
    path('create_task/', create_task, name='create_task'),
    path('', list_tasks, name='list_tasks'),
    path('detail_task/<int:task_id>', detail_task, name='detail_task'),
    path('update_task/<int:task_id>', update_task, name='update_task'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),
]
