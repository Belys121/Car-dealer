from django.contrib import admin
from .models import Brand, Comment, Offer, VehicleType, FuelType

admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Offer)
admin.site.register(VehicleType)
admin.site.register(FuelType)
