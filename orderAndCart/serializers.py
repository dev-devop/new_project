from rest_framework.serializers import ModelSerializer
from .models import Order, OrderedItem

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderedItemSerializer(ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = '__all__'