from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from customer.models import Cart,CartItem
from user.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class ShowCart(View):
    def get(self,request,pk):
        user = User.objects.get(id=pk)
        cart = Cart.objects.get(user=user)
        cartitem = CartItem.objects.filter(cart=cart)
        count = CartItem.objects.filter(cart=cart).count()   
        # count = user.cart_set.get()
        
        total = 0
        for c in cartitem:
            total += c.quantity * c.product.price
        cart.total_price = total
        context = {
            'cartitem' : cartitem,
            'cart':cart,
            'count':count,
        }
        
        return render(request,'customer/cart.html',context)
    def post(self,request,pk):
        user = User.objects.get(id=pk)
        cart = Cart.objects.get(user=user)
        cartitem = CartItem.objects.filter(cart=cart)
        cartitemid = request.POST.get('cartitem')
        remove = request.POST.get('remove')
        count = CartItem.objects.filter(cart=cart).count()
        print(count)
        if cartitemid:
            cartitemquant = CartItem.objects.get(id=cartitemid)
            if remove:
                cartitemquant.quantity =cartitemquant.quantity - 1
                
            else:
    
                cartitemquant.quantity =cartitemquant.quantity + 1
                
            cartitemquant.save()
        total = 0
        for c in cartitem:
            total += (c.quantity * c.product.price)
        cart.total_price = total
        cart.save()
        print(total)
        context = {
            'cartitem' : cartitem,
            'cart':cart,
            'count':count,
        }
        return render(request,'customer/cart.html',context)
    