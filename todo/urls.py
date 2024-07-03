from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('add-todo/', add_todo, name='add-todo'),
    path('edit-todo/<int:pk>/', edit_todo, name='edit-todo'),
    path('delete-todo/<int:pk>/', delete_todo, name='delete-todo'),
    path('complete-todo/<int:pk>/', complete_todo, name='complete-todo'),
]