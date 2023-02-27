from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpRequest
from user.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,FormView
from django.contrib import messages
from django.views import View
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import make_password, check_password

class Login(View):
    template_name = 'account/login.html'
    # form_class = Loginform
    def get(self,request):
        # form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'message': message})
    def post(self,request):
        print('************')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if check_password(password,user.password):
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('profile')
            else:
                message = 'password is wrong'
        else:
            message = 'no user found'
        return render(request, self.template_name, context={'message': message})
    
class Profile(View):
    def get(self,request):
        return render(request,'account/profile.html')
