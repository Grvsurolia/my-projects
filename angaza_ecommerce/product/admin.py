"""
@author: gaurav surolia
"""
import datetime
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from product.views import ProductSpecification
from django.contrib import admin
from .models import (Deal, Brand, Tag, Cart, Category, Size, ProductQuestion, ProductColour, ProductDescription, Colour, Product, ProductReview, ProductDeal,
                     ProductImage, ProductSize, WishList, Store, ProductCategory, Slider, SubCategories,SubProduct)
from django.contrib.admin import DateFieldListFilter
from stores.models import ProductSpecification,StoreOwner
from import_export.admin import ImportExportModelAdmin

# Register your models here.

def customTitledFilter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


class CartAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name',
                     "user__last_name", "user__email", "product__title"]
    list_filter = (("user__email", customTitledFilter('User')), )
    list_display = ("id", "user", "product", "quantity")
    list_display_links = ('id', 'user',)



admin.site.register(Cart, CartAdmin)
# admin.site.register(ProductSubProduct)


class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('name', )
    list_display_links = ('id', 'name',)
    list_display = ("id", "name")


admin.site.register(Tag, TagAdmin)


class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('name', )
    list_display_links = ('id', 'name',)
    list_display = ("id", "name")


admin.site.register(Brand, BrandAdmin)

class StoreOwnerInline(admin.StackedInline):
    model = StoreOwner
    extra = 0

class StoreAdmin(admin.ModelAdmin):
    search_fields = ['name', "owner__email",
                     "owner__first_name", "owner__last_name"]
    inlines = [StoreOwnerInline,]
    list_filter = ('name', )
    list_display_links = ('id', 'name',)
    list_display = ("id", "name", "owner", "location", "status")


admin.site.register(Store, StoreAdmin)


class DealsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('name', )
    list_display_links = ('id', 'name',)
    list_display = ("id", "name", "status")


admin.site.register(Deal, DealsAdmin)


class SizesAdmin(admin.ModelAdmin):
    search_fields = ['size_or_weight']
    list_filter = ('size_or_weight', )
    list_display_links = ('id', 'size_or_weight',)
    list_display = ("id", "size_or_weight")


admin.site.register(Size, SizesAdmin)


class ColoursAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_filter = ('name', )
    list_display_links = ('id', 'name',)
    list_display = ("id", "name", "code")


admin.site.register(Colour, ColoursAdmin)


# class ImageAdmin(admin.ModelAdmin):
#     list_display = ("id", "image")


# admin.site.register(Image, ImageAdmin)


class WishListAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name',
                     'user__last_name', "user__email", "product__title"]
    list_display_links = ('id', 'user',)
    list_filter = (("user__email", customTitledFilter('User')),
                   ('product__title', customTitledFilter('Product Name')), )
    list_display = ("id", "user", "product", "is_delete")


admin.site.register(WishList, WishListAdmin)


# class ProductQuestionAdmin(admin.ModelAdmin):
#     search_fields = ['product__title', "question"]
#     list_filter = (('product__title', customTitledFilter('Product Name')), )
#     list_display = ("id", "product", "question")


# admin.site.register(ProductQuestion, ProductQuestionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('name',)
    list_display_links = ('id', 'name',)
    list_display = ("id", "name")


admin.site.register(Category, CategoryAdmin)

class SubProductAdmin(admin.ModelAdmin):
    search_fields = ['subproduct_name']
    list_filter = ('subproduct_name',)
    # list_display_links = ('id', 'name',)
    list_display = ("id", "subproduct_name")

admin.site.register(SubProduct,SubProductAdmin)



# class ProductSizeAdmin(admin.ModelAdmin):
#     search_fields = ['product__title',"product_size__size_or_weight"]
#     list_filter = ('product__title',)
#     list_display = ("id", "product", "product_size")


# admin.site.register(ProductSize, ProductSizeAdmin)


# class Admin(admin.ModelAdmin):
#     search_fields = ['product__title',"product_colour__name"]
#     list_filter = ('product__title',)
#     list_display = ("id", "product", "product_colour")


# admin.site.register(ProductColour, ProductColourAdmin)


# class ProductImageAdmin(admin.ModelAdmin):
#     search_fields = ['product__title']
#     list_filter = ('product__title',)
#     list_display = ("id", "product", "product_image")


# admin.site.register(ProductImage, ProductImageAdmin)


# class ProductDealsAdmin(admin.ModelAdmin):
#     search_fields = ['product__name', "product_deals__name"]
#     list_filter = (('product_deals__name', customTitledFilter('Product Name')),)
#     list_display = ("id", "product", "product_deals", "status")


# admin.site.register(ProductDeal, ProductDealsAdmin)


# class ProductReviewAdmin(admin.ModelAdmin):
#     search_fields = ['deal__title', "email"]
#     list_filter = (('deal__title', customTitledFilter('Product Name')),)
#     list_display = ("id", "deal", "star_point", "name", "email")


# admin.site.register(ProductReview, ProductReviewAdmin)


# class ProductCategoryAdmin(admin.ModelAdmin):
#     search_fields = ['product__title',"product_category__name"]
#     list_display = ("id", "product", "product_category")
#     list_filter = ('product_category__name', )


# admin.site.register(ProductCategory, ProductCategoryAdmin)


# class ProductDescriptionAdmin(admin.ModelAdmin):
#     search_fields = ['product__title', "description", "title"]
#     list_filter = ('product__title', )
#     list_display = ("id", "title", "product")


# admin.site.register(ProductDescription, ProductDescriptionAdmin)


class SlidersAdmin(admin.ModelAdmin):
    list_display = ("id","url", "image")
    list_display_links = ('id', 'url',)

admin.site.register(Slider,SlidersAdmin)


class ProductDealInline(admin.StackedInline):
    model = ProductDeal
    extra = 0

class ProductSubProductLine(admin.TabularInline):
    model = SubProduct
    extra = 0

class ProductColourInline(admin.StackedInline):
    model = ProductColour
    extra = 0


class ProductDescriptionInline(admin.StackedInline):
    model = ProductDescription
    extra = 0


class ProductSizesInline(admin.StackedInline):
    model = ProductSize
    extra = 0


class ProductCategoryInline(admin.StackedInline):
    model = ProductCategory
    extra = 0


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecification
    extra = 0


class ProductQuestionInline(admin.StackedInline):
    model = ProductQuestion
    extra = 0

class ProductReviewsInline(admin.StackedInline):
    model = ProductReview
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', "store__name", "brand__name"]
    list_display_links = ('id', 'title',)
    inlines = [ProductColourInline, ProductSizesInline, ProductCategoryInline, ProductImageInline,
               ProductDescriptionInline, ProductQuestionInline, ProductSpecificationInline, ProductDealInline,ProductReviewsInline,ProductSubProductLine]
    list_filter = (('start_time', DateRangeFilter),
                   ('end_time', DateRangeFilter),
                   ('store__name', customTitledFilter('Store Name')),
                   ('brand__name', customTitledFilter('Brand Name')),)
    list_display = ("id", "title", "store", "product_option", "price",
                    "sale_price", "brand", "start_time", "end_time","created_at")
    ordering = []

    # def get_queryset(self, request):
    #     qs = super(ProductAdmin, self).get_queryset(request)
    #     return qs.filter(title__icontains='maggi')
    pass


admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductSpecification)


# subcat
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'sub_name',)
    list_display = ("id", "sub_name")

admin.site.register(SubCategories,SubCategoriesAdmin)


