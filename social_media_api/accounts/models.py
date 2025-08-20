from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=100)

     # ... additional fields and methods as required ...
    bio = models.TextField(unique=True, max_length=255)
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self',symmetrical=False, related_name='following', blank=True,)
    
    def __str__(self):
        return self.username