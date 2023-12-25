from django.contrib import admin
from django.urls import path

from news import views

urlpatterns = [
    path('', views.Home),
    path('new/<int:id>/', views.New),
]
