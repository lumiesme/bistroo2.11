from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)  # Admin page show Category model
admin.site.register(Menu)
