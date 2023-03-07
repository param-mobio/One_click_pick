import django_filters
from django_filters import filters
from .models import *
from django.db.models import Q
from products.models import Products,Category

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ('category',)


