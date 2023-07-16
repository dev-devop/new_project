from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DeliverySerializer, DestinationSerializer
from .models import Destination, Delivery


# Create your views here.


@api_view(['GET',])
def getdeliveries(request):
    delivery = Delivery.objects.order_by('order_id')
    serializer = DeliverySerializer(delivery, many= True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getdelivery(request,pk):
    data = request.data
    
    try:
        delivery = Delivery.objects.get(id=pk)
        if request.method == 'GET':
            
            serializer = DeliverySerializer(delivery, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = DeliverySerializer(delivery, data=request.data,
                                    context= {'request': request}, partial=True)
            
            if serializer.is_valid():
                # delivery.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                serializer = DeliverySerializer(delivery, data=request.data,
                                    context= {'request': request}, partial=True) 
                serializer.is_valid()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            delivery.delete()
            serializer = DeliverySerializer(delivery, many=False)
            return Response(serializer.data)
    except Delivery.DoesNotExist:
            return Response(status=400)


@api_view(['POST'])
def Createdelivery(request):
    """This is the endpoint for registering new deliveries on the platform."""

    serializer = DeliverySerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        delivery = serializer.save()
        delivery.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def getdestinations(request):
    delivery = Destination.objects.order_by('id')
    serializer = DestinationSerializer(delivery, many= True,)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getdestination(request,pk):
    data = request.data
    try:
        location = Destination.objects.get(id=pk)
        if request.method == 'GET':
            
            serializer = DestinationSerializer(location, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = DestinationSerializer(location, data=request.data,partial=True)
            
            if serializer.is_valid():
                # Destination.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            location.delete()
            serializer = DestinationSerializer(location, many=False)
            responseData = {"message":"delivery location details successfully deleted","data":""}
            return Response(data=responseData, status= status.HTTP_200_OK)
    except Destination.DoesNotExist:
            return Response(status=400)

@api_view(['POST'])
def Createdestination(request):
    """This is the endpoint for saving the address of existing deliverys."""

    serializer = DestinationSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        delivery = serializer.save()
        delivery.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

