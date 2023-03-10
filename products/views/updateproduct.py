from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import UpdateView
from products.models import Products, User
from products.forms import ProductForm
class UpdateProduct(UpdateView):
    def get(self,request,pk):
        form = ProductForm()
        products = Products.objects.get(id=pk)
        form = ProductForm(instance=products)
        context = {
            'form' : form
        }
        return render(request,'products/createProduct.html',context)
    def post(self,request,pk):
        products = Products.objects.get(id=pk)
        form = ProductForm(request.POST,request.FILES,instance=products)
        user = request.user
        print(user)
        if form.is_valid():
            product = form.save()
            product.update_by = user
            product.save()
            return redirect('index')
        context = {
            'form':form
        }
        return render(request,'products/createProduct.html',context)
