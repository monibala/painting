from django.contrib import admin

from cart.models import Cart,  coupon_code, orderinfo, review

# Register your models here.
# admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(orderinfo)
admin.site.register(review)
admin.site.register(coupon_code)