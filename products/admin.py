from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Products)