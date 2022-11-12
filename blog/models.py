from django.db import models

# Create your models here.
class Blog(models.Model):
 
    
    date = models.DateTimeField()
    img = models.ImageField(upload_to = 'Blog')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    
    
    
   
    def __str__(self):
        return str(self.title)
