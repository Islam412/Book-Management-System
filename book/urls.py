from django.urls import path

from .views import views


app_name = 'userauths'


urlpatterns = [
    path('', views.home, name='home')
]