from django.db import models
# from django.utils import timezone
import django
from user_auth.models import UserProfile
from restaurant_management.models import Restaurant, Menu

# Create your models here.

class Order(models.Model):
    status_choice = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('canceled', 'canceled')
    ]
    order_number = models.CharField(max_length=15, unique=True,)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3)
    buyer = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='order')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, related_name='order')
    timestamp = models.DateTimeField(default= django.utils.timezone.now)
    status = models.CharField(max_length=50, choices=status_choice)
    payment_status = models.CharField(max_length=50, default='no payment')

    def update_payment_status(self):
        if 'completed' in self.payment:
            self.payment_status = 'Paid'

    def __str__(self) -> str:
        return f"{self.id}"
    
    class Meta:
        ordering = ['status','id','timestamp','payment_status']

class OrderedItem(Order):
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, related_name='meal')
    product = models.CharField(max_length=400)
    quantity = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return f"{self.product}..... {self.price}"
    
    class Meta:
        ordering = ['id']
