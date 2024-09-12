from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path('sign-up/', views.RegisterView.as_view(), name='sign-up'),
    path('sign-in/', views.LoginView.as_view(), name='sign-in'),
    path('user/sign-out/', views.LogoutView.as_view(), name='sign-out'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
