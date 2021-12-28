from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import deactivate, gettext as _
# from django.contrib.postgres.fields import ArrayField

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
    
    
GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
MARITAL_STATUS = (
        ('married', 'MARRIED'),
        ('unmarried', 'UNMARRIED'), 
    )

TEAM_STATUS = (
    ("python","PYTHON"),
    ("other","OTHER"),
)

DEPARTMENT_STATUS = (
    ("technical","Technical"),
    ("non-technical","Non-Technical"),
    ("management","Management"),
    ("other","Other"),

)

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=100,choices=DEPARTMENT_STATUS, default="technical")
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class User(AbstractUser):

    username = None
    email = models.EmailField(_('Email_address'),unique=True)
    full_name = models.CharField(max_length=200,blank=True,null=True)
    employee_code = models.CharField(max_length=255,unique=True)
    profile_image = models.ImageField(blank=True,null=True,upload_to = 'upload/')
    CardID = models.CharField(max_length=255,null=True,blank=True,unique=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    designation = models.CharField(max_length=255,blank=True,null=True)
    # skills = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    # salary = models.PositiveIntegerField(default=0,blank=True,null=True)
    mobile_number = models.CharField(max_length=12,blank=True,null=True)
    alternative_number = models.CharField(max_length=12,blank=True,null=True)
    team = models.CharField(max_length=100,choices=TEAM_STATUS,blank=True,null=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES,blank=True,null=True)
    birth_date = models.DateField(null=True,blank=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,default='IN')
    pincode = models.CharField(max_length=255,blank=True,null=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    blood_group = models.CharField(max_length=255,blank=True,null=True)
    martial_status = models.CharField(max_length=100,choices=MARITAL_STATUS,blank=True,null=True, default='unmarried')
    aadhar_id = models.CharField(max_length=20,default = '0',blank=True,null=True)
    pan_no = models.CharField(max_length=10,default='0',blank=True,null=True)
    hr_common_email = models.EmailField(_('Hr Email_address'),blank=True,null=True,default='hr@externlabs.com')
    is_hr = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_ceo = models.BooleanField(default=False)
    is_cto = models.BooleanField(default=False)
    is_teamlead = models.BooleanField(default=False)
    is_bde = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    password_change = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['employee_code']
    objects = UserManager()

    class Meta:
        db_table = "User"
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = []


    def __str__(self):
        return self.employee_code




class Bankaccount(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20,unique=True, blank = True, null = True)
    ifsc = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=100)
    account_holder_name = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Bankaccount")
        verbose_name_plural = _("Bankaccounts")
        
    def __str__(self):
        return self.account_holder_name

class UpdateRequest(models.Model):
    employee= models.ForeignKey(User,on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=255,blank=True,null=True)
    mobile_number = models.CharField(max_length=12,blank=True,null=True)
    alternative_number = models.CharField(max_length=12,blank=True,null=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES,blank=True,null=True)    
    birth_date = models.DateField(null=True,blank=True)
    address = models.CharField( max_length=500,blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    pincode = models.CharField(max_length=255,blank=True,null=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    blood_group = models.CharField(max_length=255,null=True,blank=True)
    martial_status = models.CharField(max_length=100,choices=MARITAL_STATUS,blank=True,null=True, default='unmarried')   
    uid = models.CharField(max_length=12,default = '0',blank=True,null=True)
    pan_no = models.CharField(max_length=10,default="0",blank=True,null=True)
    file =models.FileField(upload_to='upload/% Y/% m/% d/')

    def __str__(self):
        return self.first_name
        


# class EmployeeSalary(models.Model):

#     employee = models.ForeignKey(User,on_delete=models.CASCADE)
#     basic = models.DecimalField(default=0)
#     net_salary = models.DecimalField(default=0)
#     fixed = models.DecimalField(default=0)
#     pf = models


    

#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
