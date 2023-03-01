from django import forms
from django.forms import ModelForm
from products.models import Products


class ProductForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": "True",
                "placeholder": "Enter product name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": "True",
                "placeholder": "Enter company  name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    size = forms.ChoiceField(
        # widget=forms.TextInput(
        #     attrs={
        #         "class": "form-control",
                # "required": "True"
        #         "placeholder": "Enter product name",
        #         "data-validation-required-message": "Please enter your name",
        #     }
        # )
    )
    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": "True",
                "placeholder": "Enter price name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    
    category = forms.ChoiceField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": "True",
                "placeholder": "Enter product name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    # image = forms.ImageField(
    #     widget=forms(
    #         attrs={
    #             "class": "form-control",
    #             "required": "True"
    #         }
    #     )
    # )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "required": "True",
                "placeholder": "Enter product name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )

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
        ]
        # fields = '__all__'
