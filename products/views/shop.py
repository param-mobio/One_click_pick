from django.shortcuts import render,redirect
from django.views import View
from products.models import Products,Category
from django.core.paginator import Paginator

class Shop(View):
    
    def get(self,request):
        products = Products.objects.all()
        category = Category.objects.all()
        size = request.GET.getlist('size')
        if size:
            print(size)
            if size == ['allsize']:
                print('***********')
                products = Products.objects.all()
            else:
                products = Products.objects.filter(size=size)
        
        
        paginator_product = Paginator(products,6) 
        page_number = request.GET.get('page')
        page_obj = paginator_product.get_page(page_number)
        context = {
            'products' : products,  
            'page_obj' : page_obj,  
            'category' : category,
        }
        # con['size'] = product.get_size_display()
        return render(request,'products/shop.html',context)
    def post(self,request):
        
        return render(request,'products/shop.html') 
