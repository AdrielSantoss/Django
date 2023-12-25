from django.shortcuts import render

def Home(request):
    return render(request, 'news/pages/home.html')

def New(request, id):
    return render(request, 'news/pages/new.html', context={
        'id': id
    })