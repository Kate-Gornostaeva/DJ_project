from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<p>Красивым быть – не значит им родиться,<br>Ведь красоте мы можем научиться.<br>"
                        "Когда красив душою Человек –<br>Какая внешность может с ней сравниться?</p>")


def test(request):
    return HttpResponse("<p>Кто жизнью бит, тот большего добьется.<br>Пуд соли съевший выше ценит мед.<br>"
                        "Кто слезы лил, тот искренней смеется.<br>Кто умирал, тот знает, что живет!</p>")

def data(request):
    return HttpResponse("<p>В одно окно смотрели двое. <br>Один увидел дождь и грязь.<br>"
                        "Другой — листвы зелёной вязь, весну и небо голубое.<br>В одно окно смотрели двое.</p>")
def index2(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')