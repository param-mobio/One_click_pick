from django.shortcuts import render
from order.forms import OrderForm
from django.views import View
from user.models import User
from customer.models import Cart


class Checkout(View):
    def get(self,request,pk):
        user  = User.objects.get(id = pk)
        form = OrderForm(instance=user)
        context = {
            'form':form,
        }
        return render(request,'order/checkout.html',context)

    def post(self,request):

        return render(request,'order/checkout.html')