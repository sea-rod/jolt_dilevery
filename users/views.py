from .forms import CustomUserForm,CustomAuthForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView



class SignUpView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class CustomLoginView(LoginView):
    form_class = CustomAuthForm
    success_url = reverse_lazy("home")
    template_name = "registration/login.html"

