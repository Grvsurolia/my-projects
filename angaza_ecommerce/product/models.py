# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

import math
from django.db.models.deletion import CASCADE
import users
from django.db import models
from django.db.models.base import Model
from users.models import User
# from admin_app.models import Categories

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "Tag"
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'

    def __str__(self):
        return self.name


DEAL_CHOICE=[("FeatureDeal", "feature deal"),
            ("PopularDeal", "popular deal"),
            ("DealOfTheMonth","Deal of the Month")]

class Deal(models.Model):
    name = models.CharField(max_length=255, unique=True,choices=DEAL_CHOICE)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "Deal"
        verbose_name = 'Deal'
        verbose_name_plural = 'Deal'

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile_number = models.CharField(max_length=13)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=255,null=True)
    location = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="store")
    describe = models.TextField()
    store_portal_admin = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "Store"
        verbose_name = 'Store'
        verbose_name_plural = 'Store'

    def __str__(self):
        return self.name







class Product(models.Model):

    Product_CHOICES = (
        ("Booking", 'Booking'),
        ("Buy", 'Buy'),
       
    )
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    price_type = models.CharField(max_length=150,blank=True,null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sale_price = models.FloatField(default=0.0)
    description = models.TextField()
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    end_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    sku = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="Advertisement")
    tags = models.ManyToManyField(Tag)
    # sub_product = models.ManyToManyField(SubProduct,blank=True)
    # extra
    depot = models.IntegerField(default=0)
    is_sale = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
    discount_percent = models.FloatField(default=0.0)
    product_option = models.CharField(max_length=255,choices=Product_CHOICES)
    visit_product = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Product"
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        if self.price or self.sale_price != 0:

            discount = (self.sale_price/self.price)*100
        
            self.discount_percent = float(discount)
            super(Product, self).save(*args, **kwargs)
        else:
            self.discount_percent = 0




class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image1 = models.ImageField(upload_to="product/images")
    product_image2 = models.ImageField(upload_to="product/images",blank=True,null=True)
    product_image3 = models.ImageField(upload_to="product/images",blank=True,null=True)
    product_image4 = models.ImageField(upload_to="product/images",blank=True,null=True)

    class Meta:
        db_table = "ProductImage"
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImage'


    def __str__(self):
        return self.product.title


class ProductDeal(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_deals = models.ForeignKey(Deal, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "ProductDeal"
        verbose_name = 'ProductDeal'
        verbose_name_plural = 'ProductDeal'


    def __str__(self):
        return self.product.title


class ProductReview(models.Model):
    deal = models.ForeignKey(Product, on_delete=models.CASCADE)
    feedback = models.TextField()
    star_point = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = "ProductReview"
        verbose_name = 'ProductReview'
        verbose_name_plural = 'ProductReview'

    def __str__(self):
        return self.deal.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = "Cart"
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    def __str__(self):
        return self.product.title


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "WishList"
        verbose_name = 'WishList'
        verbose_name_plural = 'WishList'

    def __str__(self):
        return self.product.title


class ProductDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to='description/', blank=True, null=True)

    class Meta:
        db_table = "ProductDescription"
        verbose_name = 'ProductDescription'
        verbose_name_plural = 'ProductDescription'

    def __str__(self):
        return self.product.title


class ProductQuestion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        db_table = "ProductQuestion"
        verbose_name = 'ProductQuestion'
        verbose_name_plural = 'ProductQuestion'

    def __str__(self):
        return self.product.title


class Slider(models.Model):
    image = models.ImageField(upload_to="sliders")
    url = models.URLField(max_length=255,null=True,blank=True,default="https://www.dealzmoto.com/")

    class Meta:
        db_table = "Slider"
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class Brand(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Brand"
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'


class Size(models.Model):
    size_or_weight = models.CharField(max_length=10)

    class Meta:
        db_table = "Size"
        verbose_name = 'Size'
        verbose_name_plural = 'Size'

    def __str__(self):
        return self.size_or_weight


class Colour(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    class Meta:
        db_table = "Colour"
        verbose_name = 'Colour'
        verbose_name_plural = 'Colour'

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:
        db_table = "ProductSize"
        verbose_name = 'ProductSize'
        verbose_name_plural = 'ProductSize'

    def __str__(self):
        return self.product.title


class ProductColour(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_color = models.ForeignKey(Colour, on_delete=models.CASCADE)

    class Meta:
        db_table = "ProductColour"
        verbose_name = 'ProductColour'
        verbose_name_plural = 'ProductColour'

    def __str__(self):
        return self.product_color.name + " "+self.product.title


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    bluetooth = models.BooleanField(default=False)
    battery_life = models.CharField(max_length=100)
    wireless = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product.title



class SubCategories(models.Model):
    sub_name = models.CharField(max_length=255)
    # icon = models.ImageField(upload_to='subicon/')


    def __str__(self):
        return self.sub_name 

    class Meta:
        db_table = "Sub Category"
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Category'
        

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icon/')
    subcategory = models.ManyToManyField(SubCategories,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_sub_category = models.ForeignKey(SubCategories, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'ProductCategory'
        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategory'

    def __str__(self):
        return self.product.title


class SubProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    subproduct_name= models.CharField(max_length=500)
    price = models.FloatField(default=0.0)
    sale_price = models.FloatField(default=0.0,blank=True,null=True)
    discount_percent = models.FloatField(default=0.0,blank=True,null=True)


    def __str__(self):
        return self.subproduct_name

    def save(self, *args, **kwargs) -> None:

        discount = (self.sale_price/self.price)*100
        self.discount_percent = discount
        super(SubProduct, self).save(*args, **kwargs)


# class ProductSubProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     sub_product = models.ForeignKey(SubProduct, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.product.title



