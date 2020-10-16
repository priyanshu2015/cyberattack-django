from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('reflectedcsrf/', views.reflectedcsrf, name = 'reflectedcsrf'),
    path('reflectedcsrflogin/', views.reflectedcsrflogin, name = 'reflectedcsrflogin'),
]

