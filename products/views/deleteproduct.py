from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import DeleteView
from products.models import Products, User
from products.forms import ProductForm

class DeleteProduct(View):
    def get(self,request,pk):
        products = Products.objects.get(id=pk)  
        print(products)
        products.delete()
        return redirect('products')
        # return HttpResponseRedirect(reverse('products'))
