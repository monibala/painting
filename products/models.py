from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from category.models import category_types
# Create your models here.
class product (models.Model):
    product_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='media', null=True)
    price = models.IntegerField(null=True)
    discounted_price = models.FloatField(null=True)
    description = models.CharField(max_length = 100, null=True)
    category_name = models.ForeignKey(category_types,on_delete = models.CASCADE, related_name= 'category',null=True)

