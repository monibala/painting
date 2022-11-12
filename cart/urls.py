from cart import views
from django.urls import path
urlpatterns = [
    path('show_cart', views.show_cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/',views.cart,name='add-to-cart'),
    path('decrement/',views.decrement,name='decrement'),
    path('increment/',views.increment,name='increment'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('paymentdone', views.paymentdone, name='paymentdone'),
    path('orders', views.orders, name='orders'),
]
