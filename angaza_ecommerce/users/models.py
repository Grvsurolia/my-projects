# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""
from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager)
from django.db import models
from django.db.models.fields import EmailField
from django.utils.translation import gettext as _

# from product.models import Store
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email or ("@" and ".") not in email:
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
        extra_fields.setdefault('is_active', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12,blank=True,null=True)
    profile_image = models.ImageField(upload_to="profile", blank=True)
    lastEmailOtp = models.CharField(max_length=255, blank=True)
    passsword = models.CharField(max_length=30)
    CUSTOMER = 1
    ADMIN = 2
    STOREOWNER = 3

    ROLE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
        (STOREOWNER, 'StoreOwner'),
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        db_table = "User"
        verbose_name = 'User'
        verbose_name_plural = 'User'
        ordering = []

    def __str__(self):
        return self.email


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Customer"
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'

    def __str__(self):
        return self.user.email


class CustomerAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    house_no = models.CharField(
        _('flat/house no/building/company/Apartment'), max_length=50)
    colony = models.CharField(
        _('Area/Colony/Street/Sector/Village'), max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(_('Town/City'), max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    address_type = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(
        verbose_name='email address', max_length=255, blank=True, null=True)


    class Meta:
        db_table = "Customer Address"
        verbose_name = 'Customer Address'
        verbose_name_plural = 'Customer Address'



    def __str__(self):
        return self.user.email

    


class Subscribe(models.Model):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)

    class Meta:
        db_table = "Subscribe"
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribe'



    def __str__(self):
        return self.email



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()


    class Meta:
        db_table = "Contact"
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact' 
