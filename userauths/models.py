from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)

    # Change defult django in adminbanal
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_images = models.ImageField(upload_to='Images_Profile', null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True ,blank=True)
    last_name = models.CharField(max_length=200, null=True ,blank=True)
    username = models.CharField(max_length=200, null=True ,blank=True)
    phone = models.CharField(max_length=200, null=True ,blank=True)
    
    
    def __str__(self):
        return self.user.username
    

