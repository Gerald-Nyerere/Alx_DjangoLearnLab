from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        
        user.is_staff = True 
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=100)

     # ... additional fields and methods as required ...
    bio = models.CharField(unique=True, max_length=255)
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self',symmetrical=False, related_name='following', blank=True,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()