from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome.urls')),
    path('user/', include('user_auth.urls')),
    path('delivery/', include('delivery_management.urls')),
    path('order/', include('orderAndCart.urls')),
    path('pay/', include('payment_management.urls')),
    path('restaurant/', include('restaurant_management.urls')),
    path('welcome/', include('welcome.urls')),
]
