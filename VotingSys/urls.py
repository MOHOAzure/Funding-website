"""VotingSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.urls import include, path, reverse_lazy
from django.contrib import admin
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('funding/', include('funding.urls')),
    path('admin/', admin.site.urls),
]
