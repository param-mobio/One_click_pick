from django.urls import path
from order.views import checkout,order,ownersorder
urlpatterns = [
    path('checkout/<str:pk>',checkout.Checkout.as_view(), name ='checkout'),
    path('order/<str:pk>',order.Orders.as_view(),name='order'),
    path('ownerorder/<str:pk>',ownersorder.Ownerorder.as_view(),name='ownerorder'),
]   