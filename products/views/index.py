from django.shortcuts import render
from django.views import View
from products.models import Products,Category,Section


class Index(View):
    def get(self,request):
       section = Section.objects.all()
       products = Products.objects.order_by('-created_at')
       context = {
           'section' : section,
           'products' : products,
       }
       return render(request,'products/index.html',context)