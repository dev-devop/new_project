from django.contrib import admin
from .models import UserProfile,UserLocation
# Register your models here.

class AddressInline(admin.StackedInline):
    model = UserLocation
    extra = 0

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [AddressInline]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserLocation)