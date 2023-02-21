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


class Register(CreateView):
    
    def get(self,request):
        form = Registerform()
        Groups = Group.objects.all()
        print(Groups)
        context = {
            'form': form,
        }
        return render(request, 'authentication/customer_register.html', context)
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

            
            return redirect('customer_login')
        context = {
            'form' : form
        }
        
        return render(request, 'authentication/customer_register.html', context)
    
class ProductadminRegister(CreateView):
    
    def get(self,request):
        form = Registerform()
        Groups = Group.objects.all()
        print(Groups)
        context = {
            'form': form,
        }
        return render(request, 'authentication/productAdmin_register.html', context)
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
        
        return render(request, 'authentication/productAdmin_register.html', context)



    


