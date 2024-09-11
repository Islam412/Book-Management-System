from django.urls import path

from .views import home


app_name = 'book'


urlpatterns = [
    path('', home, name='home')
]