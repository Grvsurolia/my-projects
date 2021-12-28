from django.contrib import admin

from .models import Bill, BookingForm, Order, OrderProduct, SubBill

# Register your models here.

def customTitledFilter(title):
   class Wrapper(admin.FieldListFilter):
       def __new__(cls, *args, **kwargs):
           instance = admin.FieldListFilter.create(*args, **kwargs)
           instance.title = title
           return instance
   return Wrapper


class BillInline(admin.StackedInline):
    model = Bill
    extra = 0

class OrderInline(admin.StackedInline):
    model = OrderProduct
    extra = 0

class BookingInline(admin.StackedInline):
    model = BookingForm
    extra = 0



class OrderAdmin(admin.ModelAdmin):
    inlines = [BillInline,OrderInline,BookingInline]
    list_display_links = ('id', 'customer',)
    list_display = ("id", "customer",'order_cancel',)
    list_filter = ('order_cancel',)

admin.site.register(Order,OrderAdmin)


class SubBillAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'customer',)
    list_display = ("id", "customer","total_price","discount_price",)


admin.site.register(SubBill,SubBillAdmin)

class BookingFormAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'first_name','last_name')
    list_display = ("id", "first_name",'last_name',)

admin.site.register(BookingForm,BookingFormAdmin)
