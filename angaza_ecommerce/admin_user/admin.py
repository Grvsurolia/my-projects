from django.contrib import admin
from .models import AdminUser, HomePagesAdvertisement, DetailPagesAdvertisement


class AdminUserAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', "user__last_name","user__email"]
    list_display_links = ('id', 'user',)
    list_display = ("id", 'user', 'status')

admin.site.register(AdminUser, AdminUserAdmin)


class HomePagesAdvertisementAdmin(admin.ModelAdmin):
    list_filter = ('image_number', )
    list_display_links = ('id', 'url',)
    list_display = ("id", 'url', 'image_number', 'status')

admin.site.register(HomePagesAdvertisement, HomePagesAdvertisementAdmin)


class DetailPagesAdvertisementAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'url',)
    list_display = ("id", 'url', 'status')

admin.site.register(DetailPagesAdvertisement, DetailPagesAdvertisementAdmin)


