from django.contrib import admin
from django.urls import path

from news.views import Home

urlpatterns = [
    path('', Home),
]
