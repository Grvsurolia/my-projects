from django.contrib import admin, messages
from product.models import Store

from .models import ProductSpecification, StoreOwner

# class ProductSpecificationAdmin(admin.ModelAdmin):
#     search_fields = ['product__title']
#     list_filter = ('product__title', )
#     list_display = ("id", "product", "the_json")

# admin.site.register(ProductSpecification, ProductSpecificationAdmin)


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status")
    list_display_links = ('id', 'user',)
    def make_status_false(modeladmin, request, queryset):
        queryset.update(status = False)
        messages.success(request, "Selected Record(s) Marked as Status False Successfully !!")

    def make_status_true(modeladmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected Record(s) Marked as Status True Successfully !!")

  
    admin.site.add_action(make_status_false, "Make Status False")
    admin.site.add_action(make_status_true, "Make Status True")
  
admin.site.register(StoreOwner, StoreOwnerAdmin)
