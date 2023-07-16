from django.db import models
from user_auth.models import UserProfile,UserLocation
from restaurant_management.models import Restaurant
from orderAndCart.models import Order
from extras.funcs import get_default_address
# Create your models here.

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery')
    is_delivered = models.BooleanField(default=False)
    delivery_time = models.DateField(blank=True, null=True)
    delivery_person = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='deliveries')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='deliveries_from')


    def __str__(self) -> str:
        return f"Delivery{self.id} {self.delivery_to.city}"
    
    class Meta:
        ordering = ['-is_delivered','order']
        verbose_name_plural = 'Deliveries'


class Destination(models.Model):
    address = models.CharField(max_length=200,)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    destination = models.ForeignKey(Delivery, on_delete=models.CASCADE,
                                    related_name='deliveries_to', default=get_default_address)
    
    
    def __str__(self) -> str:
        return self.address.address+" "+self.address.city
    
    class Meta:
        ordering = ['-id']
        

