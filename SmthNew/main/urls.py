
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='about'),
    path('news', views.dailynews, name='dailynews'),
    path('contact', views.contacts, name='contacts'),
]