from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from products.models import Products, User
from products.forms import ProductForm

class CreateProduct(CreateView):
    def get(self,request):
        form = ProductForm()
        created_by = {
            'created_by' : request.user,
        }
        form = ProductForm(initial=created_by)
        context = {
            'form' : form
        }
        return render(request,'products/createProduct.html',context)
    def post(self,request):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
        
        context = {
            'form':form
        }
        return render(request,'products/createProduct.html',context)
