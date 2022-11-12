from products import views
from django.urls import path
urlpatterns = [

    path('products/', views.products, name='products'),
    path('productlist/', views.productlist, name='productlist'),
    path('productdetail/<int:pk>', views.productdetail, name='productdetail'),
    path('category_detail/<int:pk>', views.category_detail, name='category_detail'),
    path('blog_category/<int:id>', views.blog_category, name='blog_category'),
]
