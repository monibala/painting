from blog import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
  
   path('blog',views.blog, name='blog')
]
