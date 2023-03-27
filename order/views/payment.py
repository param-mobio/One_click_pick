from django.shortcuts import render
from django.views import View
from user.models import User
from customer.models import Cart
from order.forms import OrderForm
from order.models import Order, OrderItem
from django.shortcuts import redirect, render
from django.contrib import messages
import razorpay

class Payment(View):
    def get(self,request,pk):    
        order = Order.objects.get(id = pk)
        form = OrderForm(instance=order)
        orderitem = OrderItem.objects.filter(order = order)
        user = order.user
        email = User.objects.filter(cart__total_price=200702.00).first()
        print(email)
        print(user)
        context = {
            'order' : order,
            'form' : form,
            'orderitem' : orderitem,
        }
        return render(request,'order/payment.html',context)
    def post(self,request,pk):
        order = Order.objects.get(id=pk)
        amount = order.total_price * 100
        client = razorpay.Client(auth=("rzp_test_WYD2T6ysRmQIjA", "P40VJloknSaMIwfINX7loxlq"))
        payment =  client.order.create({
                "amount": amount,
                "currency": "INR",
                'payment_capture': '1',
            })
        print(Payment.amount)
        return render(request,'order/payment.html',{'payment':payment})