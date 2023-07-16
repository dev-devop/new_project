from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer, OrderedItemSerializer
from .models import OrderedItem, Order

# Create your views here.

@api_view(['GET',])
def getorders(request):
    purchase = Order.objects.all()
    serializer = OrderSerializer(purchase, many= True,)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getorder(request,pk):
    data = request.data

    try:
        purchase = Order.objects.get(id=pk)
        if request.method == 'GET':

            serializer = OrderSerializer(purchase, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = OrderSerializer(purchase, data=request.data,
                                    context= {'request': request}, partial=True)

            if serializer.is_valid():
                # purchase.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                serializer = OrderSerializer(purchase, data=request.data,
                                    context= {'request': request}, partial=True)
                serializer.is_valid()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            purchase.delete()
            serializer = OrderSerializer(purchase, many=False)
            return Response(serializer.data)
    except Order.DoesNotExist:
            return Response(status=400)


@api_view(['POST'])
def Createorder(request):
    """This is the endpoint for registering new order on the platform."""

    serializer = OrderSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        purchase = serializer.save()
        purchase.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def getOrderedItem(request,pk):
    data = request.data

    try:
        item = OrderedItem.objects.get(id=pk)
        if request.method == 'GET':

            serializer = OrderedItemSerializer(item, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = OrderedItemSerializer(item, data=request.data,partial=True)

            if serializer.is_valid():
                # OrderedItem.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            item.delete()
            serializer = OrderedItemSerializer(item, many=False)
            responseData = {"message":"purchase details successfully deleted","data":""}
            return Response(data=responseData, status= status.HTTP_200_OK)
    except OrderedItem.DoesNotExist:
            return Response(status=400)
    
@api_view(['POST'])
def CreateOrderedItem(request):
    """This is the endpoint for creating a new ordered item purchase."""

    serializer = OrderedItemSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        purchase = serializer.save()
        purchase.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


