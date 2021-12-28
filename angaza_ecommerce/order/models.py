# Create your models here.
import datetime
from datetime import date, timedelta

from django.db import models
from product.models import Cart, Product, Size
from users.models import CustomerAddress, User
from users.serializers import CustomerAddressSerializer


class Order(models.Model):

    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered_date = models.DateField(auto_now_add=True)
    delivered_date = models.DateField(auto_now_add=True,null=True,blank=True)
    being_delivered = models.BooleanField(default=False)
    order_cancel = models.BooleanField(default=False)
    status = models.CharField(max_length=255,null=True,blank=True)
    buy = models.BooleanField(default=False)
    booking = models.BooleanField(default=False)


    class Meta:
        db_table = "Order"
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.customer.first_name 

class OrderProduct(models.Model):
    Status_CHOICE=[("Declain", "Declain"),
            ("Accept", "Accept")]
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=Status_CHOICE,max_length=255,null=True,blank=True)


    class Meta:
        db_table = "Order Product"
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Product'
  
    def __str__(self) :
        return self.order.customer.first_name +" " + self.product.title

class SubBill(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    discount_price = models.FloatField()
    MRP_price = models.FloatField()
    total_price = models.FloatField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "Bill"
        verbose_name = 'Bill'
        verbose_name_plural = 'Bill'

class Bill(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    discount_price = models.FloatField()
    MRP_price = models.FloatField()
    total_price = models.FloatField()
    status = models.BooleanField(default=True)

    

class BookingForm(models.Model):
    prod_name = models.CharField(max_length=200,blank=True,null=True)
    price = models.FloatField(default=0.0,blank=True,null=True)

    email = models.EmailField(max_length=255,blank=True,null=True)
    mobile_number = models.CharField(max_length=13,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)


    class Meta:
        db_table = "Booking Form"
        verbose_name = 'Booking Form'
        verbose_name_plural = 'Booking Form'

    def __str__(self) :
        return self.first_name +" " + self.last_name

 