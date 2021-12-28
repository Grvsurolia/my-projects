from django.contrib import admin

# Register your models here.
from .models import Team,Member,Invitation


admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Invitation)
