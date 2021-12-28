from django.db import models
from django.db.models.fields import PositiveIntegerField
from ecommerce_users.models import User,Coupon
from order_system.models import Order
from product_system.models import Product

# Create your models here.


class Bill(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)


PAYMENT_OPTIONS = [
    ("Other UPI IDs/ Net Banking","Other UPI IDs/ Net Banking"),
    ("Add Debit/ Credit/ATM Card","Other UPI IDs/ Net Banking"),
    ("Pay on Delivery","Pay on Delivery"),
]
class Payment(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = PositiveIntegerField()
    payment_option = models.CharField(max_length=100,choices=PAYMENT_OPTIONS)
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)

class CouponApplied(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE)