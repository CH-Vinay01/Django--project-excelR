from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder':'Product Name', 'class':'form-control'}),
            'sku': forms.TextInput(
                attrs={'placeholder':'Product ID', 'class':'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder':'3999.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder':'5', 'class':'form-control'}),
            'supplier': forms.TextInput(
                attrs={'placeholder':'Company Name', 'class':'form-control'}),
        }