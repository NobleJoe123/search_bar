from django import forms
from .models import Person, BankDetail
class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=True, label='Search Person')


class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Person 
        fields = ['name', 'email', 'address', 'phonenum', 'age', 'sex', 'image']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'address': 'Address',
            'phonenum' : 'Phone_Number',
            'age' : 'Age',
            'sex': 'Gender',
            'image' : 'image'
        }

class DetailForm(forms.ModelForm):

    class Meta:
        model = BankDetail
        fields = ['person','bank_used', 'bvn', 'nin', 'account_number']












