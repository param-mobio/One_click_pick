from django.contrib import admin
from django.urls import path,include
from authentication.views import register,login,logout,otp,resend_otp

urlpatterns = [
    path('register/',register.Register.as_view(),name='customer_register'),
    path('login/', login.Login.as_view(), name='customer_login'),
    path('logout/',logout.logoutUser.as_view(),name='logout'),
    path('profile/',login.Profile.as_view(),name='profile'),
    path('productAdminRegister/',register.ProductadminRegister.as_view(),name='productAdminRegister'),
    path('registrationOtp/',otp.Otp.as_view(),name='registrationOtp'),
    path('resend_otp/', resend_otp.resend_otp, name='resend_otp'),

]