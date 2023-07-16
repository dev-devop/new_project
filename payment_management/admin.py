from django.contrib import admin
from .models import Wallet, Payment

# Register your models here.
class PaymentInline(admin.StackedInline):
    model = Payment
    fk_name = 'sender'
    extras = 0

class WalletAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]

# class PaymentAdmin(admin.ModelAdmin):
#     inlines = [OrderInline]

admin.site.register(Wallet,WalletAdmin)
admin.site.register(Payment)