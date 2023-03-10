from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from products.models import Products, User,Colour
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
        colors = request.POST.getlist('colour')
        input_color = request.POST.get('color')
        Colour.objects.create(name=input_color)
        user = request.user
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = user
            
            product.save()
            product.colour.set(colors)
            return redirect('index')
        context = {
            'form':form
        }
        return render(request,'products/createProduct.html',context)
