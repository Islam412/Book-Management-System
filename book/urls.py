from django.urls import path
from .views import home , add_book , 

app_name = 'book'

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add_book'),

]
