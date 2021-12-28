from django.contrib import admin
from plants.models import Plant,PlantType, WishList


admin.site.register(Plant)
admin.site.register(PlantType)
admin.site.register(WishList)
