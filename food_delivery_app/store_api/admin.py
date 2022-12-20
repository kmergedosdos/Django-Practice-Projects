from django.contrib import admin

from .models import Store, Location, StoreEmail, Holiday, OpenTimePeriod

# Register your models here.
admin.site.register(Store)
admin.site.register(Location)
admin.site.register(StoreEmail)