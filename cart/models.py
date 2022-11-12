from django.db import models
from django.contrib.auth.models import User
from login.models import Customer

from products.models import product
# Create your models here.
# class Order(models.Model):
#     name = models.CharField(max_length=100,blank=True,null=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
#     productid = models.IntegerField(null=True,blank=True)
#     subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2,null=True)
#     total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2,null=True)
#     quantity = models.IntegerField(default=1)
#     fee = models.IntegerField(blank = True, null = True)
         
class Cart(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(product , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)

    def __str__(self):
        return str(self.id)    

    @property
    def total_cost(self):
        return self.quantity * self.product.price   


STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)   

class orderinfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE,null=True)
    product = models.ForeignKey(product , on_delete =models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES, default ='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.price 
    
class review(models.Model):
    produc_name = models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField(max_length=100)
    mobile_number = models.IntegerField(null=True)
    comment = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media', null=True)

class coupon_code(models.Model):
    code=models.IntegerField()
    valid_date=models.DateField()
    discount=models.IntegerField(null=True)