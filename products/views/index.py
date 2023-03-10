from django.shortcuts import render
from django.views import View
from products.models import Products
class Index(View):
    def get(self,request):
       
       return render(request,'products/index.html')