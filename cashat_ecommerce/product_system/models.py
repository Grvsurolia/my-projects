from django.db import models
from django.db.models.base import Model
from ecommerce_users.models import User

# Create your models here.

class Band(models.Model):
    band_name = models.CharField(max_length=255) 


class Categories(models.Model):
    category_name=models.CharField(max_length=255)


class Colors(models.Model):
    color_name=models.CharField(max_length=50)
    color_code = models.CharField(max_length=50)


class Sizes(models.Model):
    size_code = models.CharField(max_length=10)


class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    describation = models.TextField()
    product_category = models.ManyToManyField(Categories)
    product_band = models.ForeignKey(Band,on_delete=models.CASCADE)
    product_colors = models.ManyToManyField(Colors)
    product_sizes = models.ManyToManyField(Sizes)

    

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to="product/images")


class ProductFeedBack(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback_text = models.TextField()
    star_point = models.PositiveIntegerField()


class Cart(models.Model):
    customer =models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)