from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    phone = models.CharField(max_length=200, null=True ,blank=True)
    adress = models.CharField(max_length=200 ,null=True ,blank=True)
    verified = models.BooleanField(default=False)

    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
# create user profile automatic
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile ,sender=User)
post_save.connect(save_user_profile ,sender=User)