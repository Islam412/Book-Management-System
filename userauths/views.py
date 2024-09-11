from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from userauths.models import User
from userauths.forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'userauths/sign-up.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('book:home')

    def form_valid(self, form):
        user = form.save()
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f"Hi {user.username}, your account has been created successfully.")
            return super().form_valid(form)
        return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your registration.")
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, f"Hey {request.user.username}, you are already logged in")
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)