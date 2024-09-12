from django.urls import path
from .views import book , add_book , edit_book , delete_book 

app_name = 'book'

urlpatterns = [
    path('', book, name='book'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),

]
