from django.urls import path
from . import views

app_name = 'orderAndCart'

urlpatterns = [

    path('all', views.getorders,),
    
    path('one/create', views.Createorder,),
    path('one/<str:pk>/', views.getorder,),


    path('item/<str:pk>/', views.getOrderedItem,),
    path('item/create', views.CreateOrderedItem,),

]