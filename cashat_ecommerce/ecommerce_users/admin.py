from django.contrib import admin
from . models import Address, Coupon, User,Seller,SellerAgreement
# Register your models here.

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Coupon)
admin.site.register(SellerAgreement)
admin.site.register(Seller)
