from django.shortcuts import render
from django.views import View
from products.models import Products
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Details(View):
    def get(self,request,pk):
        products = Products.objects.get(id=pk)
        likesproduct = Products.objects.filter(category=products.category)
        color = products.colour.all()
        size = products.size.all()
        print(color)
        context = {
            'products' : products,
            'likesproduct'  :likesproduct,
            'color' : color,
            'size' : size,
        }
        return render(request,'products/shopdetail.html',context)
