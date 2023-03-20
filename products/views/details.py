from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from products.models import Products
from django.contrib import messages
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
        # cartitem = CartItem.objects.filter(product=products).values_list('product', flat=True)
        cartitem = CartItem.objects.filter(product=products)
        
        user = request.user
        cart = Cart.objects.get(user = user)
        context = {
            'products' : products,
            'likesproduct'  :likesproduct,
            'color' : color,
            'size' : size,
        }
        clothsize = request.POST['clothsize']
        clothcolor = request.POST['clothcolor']
        quantity = request.POST['quantity']
        for i in cartitem:
            if products.id ==i.product.id and cart.id ==i.cart.id and i.size == clothsize and i.colour == clothcolor:
                pass
        CartItem.objects.create(
            cart = cart,
            product = products,
            size = clothsize,
            colour = clothcolor,
            quantity = quantity,
        )
        return render(request,'products/shopdetail.html',context)
