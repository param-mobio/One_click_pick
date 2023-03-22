from django import forms
from django.forms import ModelForm
from order.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["first_name","last_name","phone","email","address1","address2"]   