from django.shortcuts import render
from django.views import View
from user.models import User
from order.models import Order, OrderItem

class Orders(View):
    def get(self,request,pk):
        user = User.objects.get(id=pk)
        order = Order.objects.filter(user=user)
        orderitem = OrderItem.objects.filter(order__in =order)
        context = {
            'order' : order,
            'orderitem' : orderitem
        }
        return render(request,'order/order.html',context)
    def post(self,request,pk):
        return render(request,'order/order.html')