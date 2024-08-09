from django.contrib import admin
from .models import Profiles


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','username','email','id')

admin.site.register(Profiles,ProfileAdmin)

# Register your models here.
