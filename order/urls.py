from django.urls import path
from order.views import checkout
urlpatterns = [
    path('checkout/<str:pk>',checkout.Checkout.as_view(), name ='checkout'),
    
]   