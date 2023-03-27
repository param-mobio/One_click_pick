from django.shortcuts import render,redirect,HttpResponseRedirect
from order.forms import OrderForm
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from user.models import User
from customer.models import Cart, CartItem
from order.models import Order, OrderItem
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings



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
            # cartitem.delete()
            dict = {
                'cartitem' : cartitem,
                'order' : order,    
            }
            html_template = 'order/orderemail.html'
            html_message = render_to_string(html_template,context=dict)
            subject = 'Order is successfully placed'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [order.user]
            messages = EmailMessage(subject, html_message, email_from, recipient_list)
            messages.content_subtype = 'html'
            messages.send()
            return HttpResponseRedirect(reverse('payment',args=[order.id]))
        context = {
            'form':form,
            'order':order,
        }
        return render(request,'order/checkout.html',context)