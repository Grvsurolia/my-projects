from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class AdminUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "Admin User"
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin User'

    def __str__(self):
        return self.user.email

Home_CHOICE=[(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7)]

class HomePagesAdvertisement(models.Model):
    image_number = models.PositiveIntegerField(choices=Home_CHOICE)
    thumbnail = models.ImageField(upload_to="Advertisement/")
    url = models.URLField(max_length=255,default="https://www.dealzmoto.com/")
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "Home Page Advertisement"
        verbose_name = 'Home Page Advertisement'
        verbose_name_plural = 'Home Page Advertisement'

    def __str__(self):
        return str(self.image_number) + " " + str(self.status)


class DetailPagesAdvertisement(models.Model):
    thumbnail = models.ImageField(upload_to="Advertisement/")
    url = models.URLField(max_length=255,default="https://www.dealzmoto.com/")
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.url

    class Meta:
        verbose_name = _("Detail Page Advertisement")
        verbose_name_plural = _("Detail Page Advertisement")