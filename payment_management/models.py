from typing import Any
from django.db import models
from user_auth.models import UserProfile
from orderAndCart.models import Order
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import django.utils.timezone
import random



# Create your models here.

class Wallet(models.Model):
    """Information about the users wallet"""
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='wallet')
    acct_number = models.BigIntegerField(null=True, unique=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    txn_history = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.owner.username} {self.acct_number}"


class Payment(models.Model):
    """The payment information for any food order."""
    payment_method = [
        ('Transfer', 'Transfer'),
        ('Card', 'Card'),
        ('Crypto', 'Crypto')
    ]
    status_choice = [
        ('completed', 'completed'),
        ('pending', 'pending'),
        ('unsuccessful', 'unsuccesful')
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=3,)
    status = models.CharField(max_length=50,choices=status_choice, default='pending')
    recipient = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='credit',)
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='debit',)
    payment_type = models.CharField(max_length=100, choices=payment_method, default='Transfer')
    fee = models.DecimalField(max_digits=10, decimal_places=3,)
    
    

    def __str__(self) -> str:
        return f"{self.order.restaurant.name} {self.amount} {self.payment_type}"

class Transfer(models.Model):
    sender = sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='sent_money')
    recipient = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='received_money',)
    amount = models.DecimalField(max_digits=10, decimal_places=2,)
    status = models.CharField(choices=Payment.status_choice, default= 'pending')
    time = models.DateTimeField(default=django.utils.timezone.now())

    def __str__(self) -> str:
        return self.amount


# class PaymentGateway(models.Model):
#     card_type = models.CharField()
#     def __str__(self) -> str:
#         return self.card_type



# class Cards(models.Model):
#     card_type = models.CharField()
#     def __str__(self) -> str:
#         return self.card_type


@receiver(post_save, sender= Transfer)
def confirm_transfer(sender, created, instance, *args, **kwargs):
    if created:
        instance.status = 'completed'
        instance.save()

@receiver(post_save, sender= Payment)
def confirm_payment(sender, created, instance, *args, **kwargs):
    if created:
        instance.status = 'completed'
        instance.order.payment_status = 'Paid'
        instance.save()

@receiver(post_save, sender= Wallet)
def confirm_payment(sender, instance, created, *args, **kwargs):
    """ Creates account numbers for every user """
    if instance.acct_number is None or len(str(instance.acct_number)) < 10 :
        
        for i in range(5):
            acct = random.randint(1230000005, 2430000005)
            try:
                wallet = Wallet.objects.get(acct_number= acct)
            except Wallet.DoesNotExist:
                instance.acct_number = acct
                instance.save()
                print('No match found')
                break
    pass


# @receiver(pre_save, sender=Payment)
# def set_default_wallet(sender, instance, **kwargs):
#     if not instance.sender.id:
#         instance.sender.id = Wallet.objects.get(owner=instance.sender.owner).id
#         print(instance)


{
"order":"5",
"amount":"250",
"status":"completed",
"recipient":"4",
"sender":"3",
"fee":"100"
}