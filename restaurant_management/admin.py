from django.contrib import admin
from orderAndCart.models import OrderedItem
from .models import Restaurant,Location, Menu, Review

# Register your models here.
class MenuInline(admin.TabularInline):
    model = Menu
    extras = 0
class ReviewInline(admin.TabularInline):
    model = Review
    extras = 0
class LocationInline(admin.TabularInline):
    model = Location
    extras = 0
class OrderedItemInline(admin.TabularInline):
    model = OrderedItem
    extras = 0

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [LocationInline,OrderedItemInline, MenuInline, ReviewInline]

# class LocationAdmin(admin.ModelAdmin):
#     inlines = [OrderedItemInline]

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Location)
admin.site.register(Menu)
admin.site.register(Review)
