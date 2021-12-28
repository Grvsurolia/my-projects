"""
@author: gaurav surolia
"""

from users.serializers import ContactSerializer
from django.contrib import admin
from .models import Contact, User, Customer, Subscribe, CustomerAddress,Contact
from django.contrib.auth.models import Group


from typing import Set

admin.site.empty_value_display = '-empty-'
admin.site.site_header = "Angaza Admin Panel"
admin.site.site_title  =  "Angaza ecommerce admin site"
admin.site.index_title  =  "Angaza Store Admin"
# admin.site.unregister(Group)





class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', "last_name", "email","phone_number","role"]
    list_filter = ('role', )
    list_display = ("id", 'email', 'first_name',
                    "last_name", "role","is_superuser","is_staff")
    list_display_links = ('id','email',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (('email','role'),'password',)
        }),
        ('Extra Details', {
            'fields': (('first_name','last_name','phone_number'),('profile_image','lastEmailOtp',))
        }),
        ('Status', {
            'fields': (('is_active','is_staff','is_superuser'),)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('groups','user_permissions','last_login', 'date_joined',),
        }),
    )
    def get_form(self, request, obj: None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
                'password'
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form


# # temp test
# class CustomerAddressInline(admin.TabularInline):
#     model = CustomerAddress

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name','user__last_name',"user__email"]
    list_display = ("id", 'user')
    list_display_links = ('id','user',)
    # inlines = [CustomerAddressInline,]



def customTitledFilter(title):
   class Wrapper(admin.FieldListFilter):
       def __new__(cls, *args, **kwargs):
           instance = admin.FieldListFilter.create(*args, **kwargs)
           instance.title = title
           return instance
   return Wrapper



class CustomerAddressAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', "user__last_name", "user__email"]
    list_filter = (("user__email",customTitledFilter('User')), )
    list_display = ("id", 'user', "house_no", 'landmark',
                    "city", "state", "country", "contact_number")
    list_display_links = ('id','user',)
    # pass
    
    


class SubscribeAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    list_display = ("id",'email')
    list_display_links = ('id','email',)


class ContactAdmin(admin.ModelAdmin):
    search_fields = ["email","subject"]
    list_display = ("id","name",'email',"subject","message")
    list_display_links = ('id','name',)





admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAddress, CustomerAddressAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Contact,ContactAdmin)
