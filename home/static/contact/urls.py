from contact import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

   path('contact', views.contact, name='contact')
]
