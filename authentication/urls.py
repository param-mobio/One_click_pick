from django.contrib import admin
from django.urls import path,include
from authentication.views import register

urlpatterns = [
    path('register/',register.Register.as_view(),name='customer_register')
]