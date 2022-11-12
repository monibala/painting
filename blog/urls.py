from blog import views
from django.urls import path
urlpatterns = [

    path('blog/', views.blog, name='blog'),
    path('blogdetail/<int:pk>', views.blogdetail, name='blogdetail'),
]
