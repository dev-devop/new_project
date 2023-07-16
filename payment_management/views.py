from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaymentSerializer, WalletSerializer, TransferSerializer
from .models import Payment, Wallet
from orderAndCart.models import Order

# Create your views here.

@api_view(['GET',])
def getwallets(request):
    wallet = Wallet.objects.order_by('-owner_id')
    serializer = WalletSerializer(wallet, many= True,)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getwallet(request,pk):
    data = request.data

    try:
        wallet = Wallet.objects.get(id=pk)
        balance = wallet.balance
        if request.method == 'GET':

            serializer = WalletSerializer(wallet, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = WalletSerializer(wallet, data=request.data,
                                    context= {'request': request}, partial=True)

            if serializer.is_valid():
                # wallet.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                serializer = WalletSerializer(wallet, data=request.data,
                                    context= {'request': request}, partial=True)
                serializer.is_valid()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            wallet.delete()
            serializer = WalletSerializer(wallet, many=False)
            return Response(serializer.data)
    except Wallet.DoesNotExist:
            return Response(status=400)


@api_view(['POST'])
def CreateWallet(request):
    """This is the endpoint for registering new deliveries on the platform."""

    serializer = WalletSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        wallet = serializer.save()
        wallet.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def getPayment(request,pk):
    data = request.data

    try:
        receipt = Payment.objects.get(id=pk)
        if request.method == 'GET':

            serializer = PaymentSerializer(receipt, many=False)
            return Response(serializer.data)
    #payment shouldn't be editable
        elif request.method == 'DELETE':
            receipt.delete()
            serializer = PaymentSerializer(receipt, many=False)
            responseData = {"message":"Payment details successfully deleted","data":""}
            return Response(data=responseData, status= status.HTTP_200_OK)
    except Payment.DoesNotExist:
            return Response(status=400)
    
@api_view(['POST'])
def makePayment(request):
    """This is the endpoint for creating new payment."""

    serializer = PaymentSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        order = serializer.validated_data['order']
        wallet = order.buyer.wallet
        amount = serializer.validated_data['amount']
        serializer.validated_data['sender'] = wallet
        #The sender automatically matches to the person on the wallet now. 
        #meaning, a person can't pay for an order that isn't theirs

        if wallet.balance >= float(amount) :
            wallet.balance = float(wallet.balance) - float(amount)

            receipt = serializer.save()
            receipt.save()
            wallet.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.error_messages['amounterror'] = 'Insufficient balance'
        return Response(serializer.error_messages['amounterror'])
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def makeTransfer(request):
    wallet =  Wallet.objects.get(acct_number= request.data['acct_number'])
    request.data['recipient'] = wallet.id
    serializer = TransferSerializer(data= request.data, context={'request':request})

    try:
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            sender = serializer.validated_data['sender']
            # serializer.validated_data['sender'], sender = 
            serializer.validated_data['recipient'] = wallet
            if sender.balance >= float(amount) :
                sender.balance = float(sender.balance) - float(amount)
                wallet.balance = float(wallet.balance)+float(amount)
                

                receipt = serializer.save()
                receipt.save()
                sender.save()
                wallet.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)
    except Wallet.DoesNotExist:
        serializer.error_messages['accounterror'] = 'Account doesn\'t exist'
        return Response(serializer.error_messages['accounterror'])


{"amount": "10", "sender": "4", "acct_number": "2030165986" ,"r": "1312210570"}