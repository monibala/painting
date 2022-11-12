from testimonial import views
from django.urls import path
urlpatterns = [

    path('testimonial/', views.testimonial, name='testimonial'),
]
