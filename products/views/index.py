from django.shortcuts import render
from django.views import View
from products.models import Products,Section
from django.db.models import Q

class Index(View):
    def get(self,request):
       section = Section.objects.all()
       product = Products.objects.all()
       products = Products.objects.order_by('-created_at')
       s = request.GET.get('search')
       pr = None
       if s is not None:
           pr = product.filter(Q(name__icontains=s) | Q(company__icontains=s))
       context = {
           'section' : section,
           'products' : products,
           'pr' : pr,
       }
       return render(request,'products/index.html',context)