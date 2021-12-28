import hashlib

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class CustomUser(AbstractUser):
    """
    Add additional fields to the user model here.
    """
    username = None
    email = models.EmailField(unique=True,max_length=500)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12,null=False,blank=False)
    company_name = models.CharField(max_length=500,null=False,blank=False)
    mailsaas_type = models.CharField(max_length=100,null=False,blank=False)
    avatar = models.FileField(upload_to='profile-pictures/', null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']



