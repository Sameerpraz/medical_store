from .models import Company
from django import forms

class FormPost(forms.ModelForm):
    class Meta:
        model = Company
        fields =('name','licence_no','address','contact_no','email','description')

        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your name here'}),
            'licence_no':forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'description':form.TextInput(attrs={'class':'form-control'}),      
        }


class FormEdit(forms.ModelForm):
    class Meta:
        model = Company
        fields =('address','contact_no','email')

        widgets={
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.Textarea(attrs={'class':'form-control'}),
        }