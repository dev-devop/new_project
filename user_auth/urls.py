from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('profile', views.getUsers,),
    path('profile/create', views.CreateUser,),
    path('profile/<str:pk>/', views.getUser,),
    path('profile/<str:pk>/update', views.getUser,),
    path('profile/<str:pk>/delete', views.getUser,),
    path('addy/<str:pk>/', views.getLocation,),
    path('addy/<str:pk>/update', views.getLocation,),
    path('addy/<str:pk>/delete', views.getLocation,),
    path('addy/create', views.CreateUserLocation,),
]
