from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.contrib.auth.models import Group,Permission
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email or ("@" and ".") not in email :
            raise ValueError('Please Provide Correct Email Format')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_active', False)
        
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)
    user_profile = models.ImageField(upload_to='upload/', max_length=1000,blank=True,null = True)
    phone_number = models.CharField(unique=True,max_length=10, null=True, blank=True)
    address = models.TextField(max_length=1000, null=True)
    is_varified = models.BooleanField(default=False)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False,)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username or self.email
    
        
class Authantication(models.Model):
    email = models.EmailField(blank=True,null=True)
    otp = models.CharField(max_length=6)
    isVerified = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
            return self.email

    def get_Mobile(self):
        return str(self.Mobile) + ' belongs to ' + self.email + ' email.'


class emailModel(models.Model):
    email = models.EmailField(unique=True,max_length=100)
    
    def __str__(self):
        return self.email


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message



