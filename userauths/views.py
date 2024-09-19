from django.views.generic.edit import FormView ,UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect ,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from userauths.models import User , Profile
from userauths.forms import UserRegisterForm , ProfileForm




class RegisterView(FormView):
    template_name = 'userauths/sign-up.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('book:book')

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
    

class LoginView(TemplateView):
    template_name = 'userauths/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are Logged In")
                return redirect('book:book')
            else:
                messages.error(request, 'Username or password does not exist.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

        return redirect('userauths:login')  # Redirect back to login on failure

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('book:book')
        return super().get(request, *args, **kwargs)
    

class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'userauths/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have been logged out')
        return redirect("userauths:sign-up")
    


class ProfileView(DetailView):
    model = Profile
    template_name = 'userauths/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)
    
    

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'userauths/profile_update.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('userauths:profile')

