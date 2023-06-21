from django import forms 
from .models import Store
from shop.models import Product



class StoreForm(forms.ModelForm):
    class  Meta:     
        model = Store
        fields = ('name','image')


class ProductForm(forms.ModelForm):
    class  Meta:     
        model = Product
        fields = ("category" ,"name" , "image" , "description", "price" ,"available")