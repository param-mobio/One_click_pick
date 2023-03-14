from django.shortcuts import render
from django.views import View
from products.models import Products
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class UserProducts(View):
    def get(self,request):
        user = request.user
        products = Products.objects.filter(created_by=user) 
        context = {
            'products' : products
        }
        return render(request,'products/products.html',context)