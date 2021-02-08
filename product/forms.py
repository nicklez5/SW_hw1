from django import forms
from product.models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title','text','created_date')