from django.shortcuts import render

from utils.factory import generate_new

def Home(request):
    generate_new()
    return render(request, 'news/pages/home.html', context= {
        "news": [generate_new() for _ in range(5)]
    })

def New(request, id):
    return render(request, 'news/pages/new.html', context={
        'id': id
    })