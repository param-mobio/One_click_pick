from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from products.models import Products
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from customer.models import Cart,CartItem
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Details(View):
    def get(self,request,pk):
        products = Products.objects.get(id=pk)
        likesproduct = Products.objects.filter(category=products.category)
        color = products.colour.all()
        size = products.size.all()
        context = {
            'products' : products,
            'likesproduct'  :likesproduct,
            'color' : color,
            'size' : size,
        }
        return render(request,'products/shopdetail.html',context)
    def post(self,request,pk):
        products = Products.objects.get(id=pk)
        likesproduct = Products.objects.filter(category=products.category)
        color = products.colour.all()
        size = products.size.all()
        user = request.user
        cart = Cart.objects.get(user = user)
        context = {
            'products' : products,
            'likesproduct'  :likesproduct,
            'color' : color,
            'size' : size,
        }
        # quantity = request.POST['quant']s
     
        clothsize = request.POST['clothsize']
        clothcolor = request.POST['clothcolor']
        quantity = request.POST['quantity']
        print(clothsize)
        print(clothcolor)
        print(quantity)
        CartItem.objects.create(
            cart = cart,
            product = products,
        )

        return render(request,'products/shopdetail.html',context)
