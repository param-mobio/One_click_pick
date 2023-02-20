from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpRequest
from user.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,FormView
from authentication.forms import Registerform
from django.views import View
from django.contrib.auth.hashers import make_password, check_password


class Register(CreateView):
    
    def get(self,request):
        form = Registerform()
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
            User.objects.create(
                email = email,
                first_name = first_name,
                last_name = last_name,
                password = make_password(password),
            )
            return redirect('customer_login')
        context = {
            'form' : form
        }
        return render(request, 'authentication/customer_register.html', context)


    


