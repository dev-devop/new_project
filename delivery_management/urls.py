from django.urls import path
from . import views

app_name = 'delivery_management'

urlpatterns = [

    path('all', views.getdeliveries,),

    path('one/create', views.Createdelivery,),
    path('one/<str:pk>/', views.getdelivery,),
    
    path('destination', views.getdestinations,),

    path('destination/<str:pk>/', views.getdestination,),
    path('destination/create', views.Createdestination,),

]