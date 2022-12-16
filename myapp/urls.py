from django.contrib import admin
from django.urls import path 
from myapp import views

urlpatterns = [
    
    path ('', views.translator , name='translator'),
    
    path ('translated', views.translated , name = 'translated'),
]
