from django.contrib import admin
from delivery_management.models import Delivery
from payment_management.models import Payment
from .models import Order, OrderedItem

# Register your models here.
class DeliveryInline(admin.TabularInline):
    model = Delivery
    extras = 0
class PaymentInline(admin.TabularInline):
    model = Payment
    extras = 0

class OrderedItemInline(admin.TabularInline):
    model = OrderedItem
    extras = 0

class OrderInline(admin.TabularInline):
    model = Order
    extras = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [PaymentInline,DeliveryInline,OrderedItemInline,]


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderedItem)