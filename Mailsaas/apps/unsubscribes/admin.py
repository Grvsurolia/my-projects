from django.contrib import admin

from .models import UnsubcribeCsv, UnsubscribeEmail

# Register your models here.
admin.site.register(UnsubscribeEmail)
admin.site.register(UnsubcribeCsv)
