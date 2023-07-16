from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RestaurantSerializer, LocationSerializer, MenuSerializer, ReviewSerializer
from .models import Location, Restaurant

# Create your views here.

@api_view(['GET',])
def getRestaurants(request):
    restaurant = Restaurant.objects.order_by('name')
    serializer = RestaurantSerializer(restaurant, many= True,)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getRestaurant(request,pk):
    data = request.data

    try:
        restaurant = Restaurant.objects.get(id=pk)
        if request.method == 'GET':

            serializer = RestaurantSerializer(restaurant, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = RestaurantSerializer(restaurant, data=request.data,
                                    context= {'request': request}, partial=True)

            if serializer.is_valid():
                # restaurant.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                serializer = RestaurantSerializer(restaurant, data=request.data,
                                    context= {'request': request}, partial=True)
                serializer.is_valid()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            restaurant.delete()
            serializer = RestaurantSerializer(restaurant, many=False)
            return Response(serializer.data)
    except Restaurant.DoesNotExist:
            return Response(status=400)


@api_view(['POST'])
def CreateRestaurant(request):
    """This is the endpoint for registering new deliveries on the platform."""

    serializer = RestaurantSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        restaurant = serializer.save()
        restaurant.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def getLocation(request,pk):
    data = request.data

    try:
        location = Location.objects.get(id=pk)
        if request.method == 'GET':

            serializer = LocationSerializer(location, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = LocationSerializer(location, data=request.data,partial=True)

            if serializer.is_valid():
                # Location.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            location.delete()
            serializer = LocationSerializer(location, many=False)
            responseData = {"message":"Location details successfully deleted","data":""}
            return Response(data=responseData, status= status.HTTP_200_OK)
    except Location.DoesNotExist:
            return Response(status=400)
    
@api_view(['POST'])
def CreateLocation(request):
    """This is the endpoint for creating new Location."""

    serializer = LocationSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        location = serializer.save()
        location.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
