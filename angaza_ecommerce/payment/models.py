from re import M

from django.db import models
from order.models import Bill, Order
from users.models import User


class MPayment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    BusinessShortCode = models.IntegerField(default=174379)
    Password = models.CharField(max_length=255)
    Timestamp = models.CharField(max_length=255)
    TransactionType = models.CharField(max_length=255,default="CustomerPayBillOnline")
    Amount = models.IntegerField(default=1)
    PartyA = models.IntegerField()
    PartyB = models.IntegerField(default=174379)
    PhoneNumber = models.IntegerField()
    CallBackURL = models.URLField(default="http://54.70.54.216:3000/callback/")
    AccountReference = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = "MPayment"
        verbose_name = 'MPayment'
        verbose_name_plural = 'MPayment'
