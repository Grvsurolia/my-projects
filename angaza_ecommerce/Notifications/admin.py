from django.contrib import admin
from .models import Notification
# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', "user__last_name","user__email"]
    list_display_links = ('id', 'user',)
    list_display = ("id", 'user')

admin.site.register(Notification, NotificationAdmin)
