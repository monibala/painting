from django.db import models
# from django.utils.text import slugify
# Create your models here.
# import random ,string
# def get_random_string(size):
#     return ''.join(random.choices(string.ascii_uppercase +
#                              string.digits, k = size))
# def unique_slug_generator(instance, new_slug=None):
#     """
#     This is for a Django project and it assumes your instance 
#     has a model with a slug field and a title character (char) field.
#     """
#     slug=slugify(new_slug)[:50]
#     Klass = instance
#     qs_exists = Klass.objects.filter(slug=slug).exists()
#     if qs_exists:
#         new_slug = slugify(str(slug)[:46]+get_random_string(4))
#         return unique_slug_generator(instance, new_slug=new_slug)
#     return slug


class category_types(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(default=1)
    # slug = models.SlugField(blank=True)
    # def save(self, *args, **kwargs):
    #     if self.slug == '':
    #         self.slug = unique_slug_generator(category_types,self.name)
    #     super(category_types, self).save(*args, **kwargs)
    def __str__(self):
        return self.category_name