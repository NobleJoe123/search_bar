from django import forms
from .models import Search
class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=True, label='Search Product')


class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Search
        fields = ['name', 'description', 'price']
        labels = {
            'name': 'product_name',
            'description': 'product_description',
            'price': 'product_price'
        }


