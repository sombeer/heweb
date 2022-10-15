from dataclasses import dataclass
from email.mime import image
from tkinter import Widget
from unicodedata import category
from django import forms
from .models import Products


class AddProductForm(forms.ModelForm):
    image = forms.ImageField(widget = forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model               = Products
        fields              =['category','product_name','Image_alt','image'] 
        labels              ={'product_name':'Product Name '}
        help_text           ={'Image_alt':'Please enter alt tag name for better seo'}
        error_messages      ={'product_name':{'required': 'Please fill the product name'},
                                'image':{'required': 'Please select the image'}} 
        widgets              ={
                                'category':forms.Select(attrs={'class':'form-control'}),
                                'product_name':forms.TextInput(attrs={'class':'form-control'}),
                                
                             }     
       