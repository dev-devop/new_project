from local_validation import newPasswordValidator
from django.contrib.auth import password_validation
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class UserProfileSerializer(ModelSerializer):
    password = serializers.CharField(max_length= 20)
    
    
    class Meta:
        model = UserProfile
        fields= ['id','username','first_name','last_name', 'password','contact', 'picture', 'is_customer']

    def validate_password(self, value):
        # user = self.context['request'].user
        """This self.context is a hidden method called by the serializer on instantiation
        it is an empty dictionary that eventually contains some details after initialization.
        You can add or remove content to it also."""
        password_validation.validate_password(value,)
        newPasswordValidator(value)
        return value

class UserLocationSerializer(ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
    
