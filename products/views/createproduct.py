from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from products.models import Products
from products.forms import ProductForm

class CreateProduct(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'products/createProduct.html'
    success_url = '/'
    def form_valid(self, form: ProductForm):

        return super().form_valid(form)
