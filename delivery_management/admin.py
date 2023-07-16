from django.contrib import admin
from .models import Delivery,Destination

# Register your models here.
class DestinationInline(admin.StackedInline):
    model = Delivery
    extras = 0
class DeliveryAdmin(admin.ModelAdmin):
    inlines = [DestinationInline]




admin.site.register(Delivery)
admin.site.register(Destination)