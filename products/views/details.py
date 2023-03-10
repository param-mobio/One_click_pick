from django.shortcuts import render,redirect
from django.views import View
from products.models import Products,Category,Colour

class Details(View):
    def get(self,request,pk):
        products = Products.objects.get(id=pk)
        likesproduct = Products.objects.filter(category=products.category)
        color = products.colour.all()
        print(color)
        context = {
            'products' : products,
            'likesproduct'  :likesproduct,
            'color' : color
        }
        return render(request,'products/shopdetail.html',context)
