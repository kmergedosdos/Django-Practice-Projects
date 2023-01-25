from django.contrib import admin

from .models import MenuConfig, Menu, Category

# Register your models here.
admin.site.register(MenuConfig)
admin.site.register(Menu)
admin.site.register(Category)