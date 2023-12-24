from django.shortcuts import render

def Home(request):
    return render(request, 'news/pages/home.html')