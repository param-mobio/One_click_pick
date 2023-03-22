from django.shortcuts import render
from order.forms import OrderForm
from django.views import View
from user.models import User
from customer.models import Cart, CartItem
from order.models import Order, OrderItem
from products.models import Products

class Ownerorder(View):
    def get(self,request,pk):
        user  = User.objects.get(id=pk)
        products = Products.objects.filter(created_by=user)
        orderitem = OrderItem.objects.filter(product__in = products)
        context = {
            'orderitem' : orderitem,
        }
        return render(request,'order/ownerorder.html',context)
    def post(self,request,pk):
        user  = User.objects.get(id=pk)
        products = Products.objects.filter(created_by=user)
        orderitem = OrderItem.objects.filter(product__in = products)
        status  = request.POST.get('status')
        id  = request.POST.get('id')
        oi = OrderItem.objects.get(id=id)
        
        oi.status = status
        oi.save()
        
        context = {
            'orderitem' : orderitem,
        }
        return render(request,'order/ownerorder.html',context)
