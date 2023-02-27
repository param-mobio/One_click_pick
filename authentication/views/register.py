from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpRequest
from user.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,FormView
from authentication.forms import Registerform
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import Group
from authentication.helpers import send_verification_otp
from django.urls import reverse
import math
import random


class Register(CreateView):
    
    def get(self,request):
        form = Registerform()
        context = {
            'form': form,
        }
        return render(request, 'account/signup.html', context)
    def post(self,request):
        
        form=Registerform(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('confirm_password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            groups = Group.objects.get(name ='customer')

            user = User.objects.create(

                email = email,
                first_name = first_name,
                last_name = last_name,
                password = make_password(password),
                
            )
            user.groups.add(groups)
            digits = "0123456789"
            otp = ""
            i=0
            for i in range(4): 
                otp+=digits[math.floor(random.random()*10)]
            otp = int(otp)
            user.otp = otp
            user.save()
            print(user.email)
            send_verification_otp(email, otp)
            value ={
                'email' : email,
                'otp' : otp
            }
            print('************')
            # return redirect('registrationOtp')   
            return render(request,'account/otp.html',value)   
        context = {
            'form' : form
        }
        
        return render(request, 'account/signup.html', context)
    
class ProductadminRegister(CreateView):
    
    def get(self,request):
        form = Registerform()
        Groups = Group.objects.all()
        print(Groups)
        context = {
            'form': form,
        }
        return render(request, 'account/signup.html', context)
    def post(self,request):
        
        form=Registerform(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('confirm_password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            groups = Group.objects.get(name ='product_admin')

            user = User.objects.create(

                email = email,
                first_name = first_name,
                last_name = last_name,
                password = make_password(password),
                
            )
            user.groups.add(groups) 
            
            
            return redirect('customer_login')
        context = {
            'form' : form
        }
        
        return render(request, 'account/productAdmin_register.html', context)



    


