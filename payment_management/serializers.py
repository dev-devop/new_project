from rest_framework.serializers import ModelSerializer
from .models import Payment,Wallet, Transfer

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['amount', 'recipient', 'sender']
