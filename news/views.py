from django.shortcuts import render

from utils.factory import generate_new

from .models import New

def Home(request):
    news = New.objects.all().order_by('-id')
    return render(request, 'news/pages/home.html', context = {
        "news": news
    })

def NewPage(request, id):
    return render(request, 'news/pages/new.html', context = {
        'id': id
    })