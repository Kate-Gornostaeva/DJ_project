
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('data', views.data),
    path('index2', views.index2),
    path('new', views.new),
]