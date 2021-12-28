from django.contrib import admin
from .models import Band,Categories,Colors,Sizes,Product,ProductFeedBack,ProductImage,Cart

# Register your models here.
admin.site.register(Band)
admin.site.register(Categories)
admin.site.register(Colors)
admin.site.register(Sizes)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductFeedBack)
admin.site.register(Cart)
