from django import forms

from .models import Product




class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=True, label='Search Product')


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']