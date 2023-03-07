from django.shortcuts import render,redirect
from django.views import View
from products.models import Products,Category
from django.core.paginator import Paginator
from products.filter import CategoryFilter

class New(View):
    def get(self,request):
        products = Products.objects.all()
        category = Category.objects.all()
        size = request.GET.getlist('size')
        if size:
            if size == ['allsize']:
                products = Products.objects.all()
            else:
                products = Products.objects.filter(size__in=size)
        category_filter = CategoryFilter(request.GET,queryset = products)
        products = category_filter.qs
        context = {
            'products' : products,  
            'category' : category,
            'category_filter' : category_filter,
        }
        # con['size'] = product.get_size_display()
        return render(request,'products/new.html',context)
    def post(self,request):
        return render(request,'products/new.html') 
