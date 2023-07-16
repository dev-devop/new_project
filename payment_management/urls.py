from django.urls import path
from . import views

app_name = 'payment_management'

urlpatterns = [

    path('wallets', views.getwallets,),

    path('wallet/create', views.CreateWallet,),
    path('wallet/<str:pk>/', views.getwallet,),


    path('receipt/<str:pk>/', views.getPayment,),
    path('receipt/create', views.makePayment,),

    path('transfer', views.makeTransfer),
]