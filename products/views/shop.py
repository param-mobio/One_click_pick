from django.shortcuts import render,redirect
from django.views import View
from products.models import Products,Category
from django.core.paginator import Paginator
from products.filter import CategoryFilter,SectionFilter
from django.db.models import Q
class Shop(View):
    
    def get(self,request):
        products = Products.objects.all()
        if products is None:
            products.delete()
        category = Category.objects.all()
        s = request.GET.get('search')
        if s!=None:
            search_product = products.filter(Q(name__icontains=s) | Q(company__icontains=s) | Q(category__name__icontains=s))
        else:
            search_product = Products.objects.all()
        
        size = request.GET.getlist('size')
        if size:
            if size == ['allsize']:
                size_product = Products.objects.all()
            else:
                size_product = Products.objects.filter(size__in=size)
        else:
            size_product = Products.objects.all()
       
        category_filter = CategoryFilter(request.GET,queryset = products)
        section_filter = SectionFilter(request.GET,queryset=products)
        category_products = category_filter.qs
        section_products = section_filter.qs
        search_size_product = search_product.intersection(size_product)
       
        filter_product = category_products.intersection(section_products)
       
        products = filter_product.intersection(search_size_product)
        
        
        paginator_product = Paginator(products,6) 
        page_number = request.GET.get('page')
        page_obj = paginator_product.get_page(page_number)
        context = {
            'products' : products,  
            'page_obj' : page_obj,  
            'category' : category,  
            'category_filter' : category_filter,
            'section_filter' : section_filter,
            's' : s,
        }
        # con['size'] = product.get_size_display()
        return render(request,'products/shop.html',context)
    
