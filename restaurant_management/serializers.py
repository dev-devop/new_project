from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Menu, Location, Restaurant, Review


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields= '__all__'

   
class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields= '__all__'

   
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        