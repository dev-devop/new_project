from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user_auth.models import UserProfile
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    contact = models.CharField(max_length=20, )
    opening_hours = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    # account = models.OneToOneField()

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    address = models.CharField(max_length=100,unique=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.restaurant.name} at {self.city}"


class Menu(models.Model):
    items = models.CharField(max_length=200)
    price = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.restaurant.name} Menu"

class Review(models.Model):
    comments = models.TextField()
    rating = models.DecimalField(max_digits=2,decimal_places=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    customer = models.ForeignKey(UserProfile, related_name='customer', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE, related_name='reviews', default='')

    def __str__(self) -> str:
        return f"{self.customer.username} review on {self.restaurant.name}"
