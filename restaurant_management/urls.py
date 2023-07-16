from django.urls import path
from . import views

app_name = 'RestaurantAndCart'

urlpatterns = [

    path('all', views.getRestaurants,),
    
    path('one/create', views.CreateRestaurant,),
    path('one/<str:pk>/', views.getRestaurant,),
   
    path('address/<str:pk>/', views.getLocation,),
    path('address/create', views.CreateLocation,),
]