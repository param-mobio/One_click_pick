from django.urls import path,include
from customer.views import profile 


urlpatterns = [
    path('customer/<str:pk>',profile.CustomerProfile.as_view(),name="cprofile"),

]