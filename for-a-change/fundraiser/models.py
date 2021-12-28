# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator



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

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                   'email': 'email'}
    

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=50)
    user_profile = models.ImageField(upload_to='upload/', max_length=1000)
    phone_number = models.CharField(max_length=10)
    lastEmailOtp = models.CharField(max_length=6,blank=True, null=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email or self.username


class Fundraiser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.CharField(max_length=50, unique=True, blank=False)
    CAMPGAIN_CAUSE = (
        ('medical', 'MEDICAL'),
        ('ngo', 'NGO'),
    )
    cause = models.CharField(max_length=20, choices=CAMPGAIN_CAUSE)
    beneficiaryFullName = models.CharField(max_length=50, unique=False)
    beneficiaryAge = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    beneficiaryGender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cityOfResidence = models.CharField(max_length=100)
    goalAmount = models.FloatField(null=False,validators=[MinValueValidator(200)])
    is_active = models.BooleanField(default=False)
    story = models.TextField(max_length=1000)
    isPrivate = models.BooleanField(default=False)
    beneficiaryPhoto = models.ImageField(upload_to='patientImg',blank=False, null=False)
    lastDateToFund = models.CharField(max_length=100)
    beneficiaryDocument = models.FileField(upload_to='documentImg',blank=False, null=False)
    created_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class frComments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, unique=False)
    created_date_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.fundraiser)