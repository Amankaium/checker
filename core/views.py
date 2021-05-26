from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class HomeView(TemplateView):
    template_name = "core/homepage.html"


class SignInView(LoginView):
    template_name = "auth/login.html"


class SignOutView(LogoutView):
    next_page = "/"
    
