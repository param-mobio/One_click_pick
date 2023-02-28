from user.models import User
from django.views import View
from django.shortcuts import render,redirect
from django.contrib import messages
from authentication.helpers import send_verification_otp
# from register import val
import math
import random


def generate_otp():
    digits = "0123456789"
    otp = ""
    i=0
    for i in range(4): 
        otp+=digits[math.floor(random.random()*10)]
    otp = int(otp)
    return int(otp)

class Otp(View):
    def get(self,request):
        
        return render(request,'account/otp.html')
    
    def post(self,request):
        # otp = request.POST.get('otp')
        realotp = request.POST.get('realotp')
        email = request.POST.get('email')
        user= User.objects.get(email=email)

        # clickbutton = request.POST.get('submit')
        if 'resendotp' in request.POST:
            otp = generate_otp()
            User.objects.filter(email=email).update(otp = otp)
            send_verification_otp(email, otp)
        if 'submit' in request.POST: 
            if realotp:
                otp = user.otp
                if(otp == int(realotp)):
                    user = User.objects.get(otp=otp)
                    user.is_active = True
                    user.save()
                    return redirect('customer_login')
            error_message = 'Otp is wrong please try again'
            context = {
            'error_message' : error_message,    
            'otp' : otp,
            'email' : email,
            }
            return render(request,'account/otp.html',context)
        error_message = 'Email has been sent'
        context = {  
            'error_message':error_message,
            'otp' : otp,
            'email' : email,
        }
        return render(request,'account/otp.html',context)
        

