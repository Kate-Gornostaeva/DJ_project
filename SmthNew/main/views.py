from django.shortcuts import render


def index(request):
    data={
        'caption': 'Первая страница'

    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

def daily(request):
    return render(request, 'main/daily.html')

def contacts(request):
    return render(request, 'main/contacts.html')