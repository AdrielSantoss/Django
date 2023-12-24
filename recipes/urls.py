from django.contrib import admin
from django.urls import include, path

from recipes.views import home

urlpatterns = [
    path('', home),
]
