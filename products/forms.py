from django import forms
from django.forms import ModelForm
from products.models import Products
from products.models import Category
import requests
SIZE = (
        ('','Select size'),
        ('Small','S'),
        ('Medium','M'),
        ('Larger','L'),
        ('Extra Large','XL'),
        ('XLL','XXL'),
    )


class ProductForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter product name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter company  name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    size = forms.CharField(
        widget=forms.Select(choices=SIZE,
            attrs={
                "class": "form-control form-select mb-3",
            }
        )
    )
    price = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter price",
                "data-validation-required-message": "Please enter product price",
            }
        )
    )
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select category",required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control form-select mb-3",
                
            }
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter Description Here",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    # created_by = forms.CharField(
    #     widget=forms.TextInput(
    #     attrs={
    #         "class": "form-control mb-3",
    #         "required": "True",
    #         "data-validation-required-message": "Please enter your name",
    #         "disabled":"True",
    #     }
    #     )
    # )
    class Meta:
        model = Products
        fields = [
            "name",
            "company",
            "size",
            "price",
            "category",
            "image",
            "description",
            # "created_by",
        ]

