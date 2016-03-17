from django.contrib import admin
from .models import *

#Sites register to validate the classes fields in the database
class SitesRegister(admin.ModelAdmin):
    fields = ['url']

admin.site.register(Sites, SitesRegister)
