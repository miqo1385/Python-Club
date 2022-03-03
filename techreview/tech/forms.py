from django import forms
from .models import ProductType, Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'