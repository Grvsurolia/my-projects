import jsonfield
from django.db import models
from product.models import Product, Store
from users.models import User


class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    # product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = "StoreOwner"
        verbose_name = 'StoreOwner'
        verbose_name_plural = 'StoreOwner'

    def __str__(self):
        return self.user.first_name + " "+self.user.last_name


class ProductSpecification(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    the_json = jsonfield.JSONField()

    class Meta:
        db_table = "ProductSpecification"
        verbose_name = 'ProductSpecification'
        verbose_name_plural = 'ProductSpecification'

    def __str__(self) -> str:
        return self.product.title
