from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpRequest
from user.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from authentication.forms import Registerform

class Register(CreateView):
    model = User
    form_class = Registerform
    template_name = 'authentication/customer_register.html'
    
    def form_valid(self, form: Registerform):

        return super().form_valid(form)

