from django import forms
from .models import BioData
class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=True, label='Search Person')


class CreateForm(forms.ModelForm):
    
    class Meta:
        model = BioData 
        fields = ['name', 'email', 'address', 'phonenum', 'age', 'sex']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'address': 'Address',
            'phonenum' : 'Phone_Number',
            'age' : 'Age',
            'sex': 'Sex'
        }


