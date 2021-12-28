from django.contrib import admin
from .models import MPayment
# Register your models here.


class MPaymentAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'BusinessShortCode',)
    list_display = ("id", "BusinessShortCode", "Timestamp","TransactionType","Amount","PartyA","PartyB")

admin.site.register(MPayment,MPaymentAdmin)