from django.shortcuts import render,redirect
from django.views import View
from products.models import Products,Category

class Details(View):
    def get(self,request,pk):
        products = Products.objects.get(id=pk)
        context = {
            'products' : products
        }
        return render(request,'products/shopdetail.html',context)
