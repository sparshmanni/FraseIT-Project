from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('new/',views.new,name='new'),
    path('about/',views.about,name='about'),
    path('tryy/',views.tryy,name='tryy')
]