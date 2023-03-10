from django.shortcuts import render,redirect
from products.forms import ProductForm
from django.views.generic.edit import UpdateView
from django.views import View
from products.models import Products

class UserProducts(View):
    def get(self,request):
        user = request.user
        products = Products.objects.filter(created_by=user) 
        context = {
            'products' : products
        }
        return render(request,'products/products.html',context)