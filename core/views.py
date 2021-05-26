from django.db.models import query
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers 

from .models import Url


class HomeView(TemplateView):
    template_name = "core/homepage.html"


class SignInView(LoginView):
    template_name = "auth/login.html"


class SignOutView(LogoutView):
    next_page = "/"


class UrlsListView(LoginRequiredMixin, ListView):
    template_name = "core/urls.html"
    
    def get_queryset(self):
        return Url.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_serializer = serializers.get_serializer("json")()
        
        context["urls"] = json_serializer.serialize(
            self.get_queryset().filter(is_paused=False),
            ensure_ascii=False
        )

        return context
