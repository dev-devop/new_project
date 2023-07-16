from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLocationSerializer, UserProfileSerializer
from .models import UserProfile, UserLocation
from django.http import HttpResponse, Http404


# Create your views here.


@api_view(['GET',])
def getUsers(request):
    user = UserProfile.objects.order_by('username')
    serializer = UserProfileSerializer(user, many= True,)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getUser(request,pk):
    data = request.data
    
    try:
        user = UserProfile.objects.get(id=pk)
        if request.method == 'GET':
            
            serializer = UserProfileSerializer(user, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserProfileSerializer(user, data=request.data,
                                    context= {'request': request}, partial=True)
            
            """I dont need the context dict here anymore because
            I already removed the line that uses it to assign data to the 'user' variable
            in serializer.py"""

            if serializer.is_valid():
                # user.update(request.data) (update works wen u know the fields being updated)
                if 'password' in request.data:
                    user.set_password(request.data['password'])
                serializer.save()
                serializer = UserProfileSerializer(user, data=request.data,
                                    context= {'request': request}, partial=True) 
                serializer.is_valid()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            user.delete()
            serializer = UserProfileSerializer(user, many=False)
            return Response(serializer.data)
    except UserProfile.DoesNotExist:
            return Response(status=400)


@api_view(['POST'])
def CreateUser(request):
    """This is the endpoint for registering on the platform as a valid member."""

    serializer = UserProfileSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def getLocation(request,pk):
    data = request.data
    
    try:
        location = UserLocation.objects.get(id=pk)
        if request.method == 'GET':
            
            serializer = UserLocationSerializer(location, many=False)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserLocationSerializer(location, data=request.data,partial=True)
            
            if serializer.is_valid():
                # userLocation.update(request.data) (update works wen u know the fields being updated)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            location.delete()
            serializer = UserProfileSerializer(location, many=False)
            responseData = {"message":"User Location details successfully deleted","data":""}
            return Response(data=responseData, status= status.HTTP_200_OK)
    except UserLocation.DoesNotExist:
            return Response(status=400)
    
@api_view(['POST'])
def CreateUserLocation(request):
    """This is the endpoint for saving the address of existing users."""

    serializer = UserLocationSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.save()
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

a = {
"state":"Lagos",
"country":"9ja",
"city":"Lekki",
"address":"victoria island",
"zip_code":"1122330"
}

b = {
"id": 29,
"username": "1user29",
"first_name": "Adebola129",
"last_name": "hop1",
"password": "SHA256SHA256",
"contact": "080790187",
"is_customer": "False"
}