from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,AbstractUser
from django.db.models.fields import EmailField
from django.utils.translation import gettext as _
# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_superuser', False) 
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        created_user = self._create_user(email, password, **extra_fields)

        return created_user


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,)
    phone_number = models.CharField(max_length=12,unique=True)
    profile_image = models.ImageField(upload_to="profile",blank=True)
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    objects = UserManager()

    class Meta:
        db_table = "User"
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = []

    def __str__(self):
        return self.email



class SellerAgreement(models.Model):
    name = models.CharField(max_length=255)
    agreement_file = models.FileField(upload_to="agreement/files") 

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    business_name = models.CharField(_('Company name/Business name'),max_length=255)
    seller_agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    house_no = models.CharField(_('flat/house no/building/company/Apartment'),max_length=50)
    colony = models.CharField(_('Area/Colony/Street/Sector/Village'),max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(_('Town/City'),max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    address_type = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

class Coupon(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    coupon_code = models.CharField(max_length=20)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return self.coupon_code