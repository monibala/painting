from django.db import models

# Create your models here.
class contact_info(models.Model):
    
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    subject=models.CharField(max_length=500,null=True)
    msg=models.TextField(max_length=100,null=True)
    def __str__(self):
        return self.name
