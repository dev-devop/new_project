from rest_framework.serializers import ModelSerializer
from .models import Delivery, Destination


class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields= '__all__'

   
class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
