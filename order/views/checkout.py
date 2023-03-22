from django.shortcuts import render
from order.forms import OrderForm
from django.views import View
from user.models import User
from customer.models import Cart, CartItem
from order.models import Order, OrderItem


class Checkout(View):
    def get(self,request,pk):
        cart  = Cart.objects.get(id = pk)
        form = OrderForm(instance=cart.user)
        context = {
            'form':form,
        }
        return render(request,'order/checkout.html',context)

    def post(self,request,pk):
        cart = Cart.objects.get(id = pk)
        cartitem = CartItem.objects.filter(cart=cart)
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = cart.user
            order.total_price = cart.total_price
            order.save()
            for i in cartitem:
                orderitem = OrderItem(product = i.product, order = order,size =i.size, colour=i.colour,quantity=i.quantity)
                orderitem.save()    
            
            cartitem.delete()
        context = {
            'form':form,
        }
        return render(request,'order/checkout.html',context)