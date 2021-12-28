from django.contrib import admin

from .models import CustomUser,emailModel,Authantication,Message


admin.site.register(Authantication)
admin.site.register(CustomUser)
admin.site.register(emailModel)
admin.site.register(Message)





