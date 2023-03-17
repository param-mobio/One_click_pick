from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from productowner.forms import ProfileForm
from user.models import User
from django.contrib import messages

class AddProduct(View):
    def get(self,request):
        return render(request,'customer/')