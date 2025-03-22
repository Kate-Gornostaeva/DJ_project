from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data={
        'caption': 'Первая страница'

    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

def dailynews(request):
    return render(request, 'main/dailynews.html')

def contacts(request):
    return render(request, 'main/contacts.html')