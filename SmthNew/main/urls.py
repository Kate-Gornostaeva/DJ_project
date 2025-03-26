
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='about'),
    #path('daily', views.daily, name='daily'),
    path('contact', views.contacts, name='contacts'),
]