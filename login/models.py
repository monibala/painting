from django.db import models
from random import choices
from django.contrib.auth.models import User
# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Islands' , 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunchal Pradesh' , 'Arunchal Pradesh'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Chandigarh' , 'Chandigarh'),
    ('Chattishgarh' , 'Chattishgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu' , 'Daman and Diu'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('punjab','punjab'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Telangana','Telangana'),
    ('West Bengal','West Bengal')
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile= models.IntegerField(null=True)
    locality = models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    zipcode= models.IntegerField()
    state= models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return str(self.id)