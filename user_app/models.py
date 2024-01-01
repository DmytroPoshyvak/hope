from django.db import models
from django.contrib.auth.models import AbstractBaseUser , AbstractUser
from django.urls import reverse , reverse_lazy
from django.utils.text import slugify

class Sex(models.Model):
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.sex

class MyCustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True)
    email = models.EmailField(null=True)
    sex = models.ForeignKey(Sex , on_delete=models.CASCADE , null=True)
    slug = models.SlugField(null=True)
    phone = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse('user' , kwargs={'slug' : self.slug })
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.email