from django.db.models.base import Model
from product_system.models import Product
from django.db import models
from ecommerce_users.models import User,Address,Coupon

class OrderItem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.customer.email

class Order(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address,on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    ordered_date = models.DateField(auto_now_add=True)
    delivered_date = models.DateField(auto_now_add=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_request = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.order_item.customer.email

class Refund(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    reason = models.TextField()
    return_item = models.BooleanField(default=False)
    refund_money = models.BooleanField(default=False)
    refund_amount = models.PositiveIntegerField()

    