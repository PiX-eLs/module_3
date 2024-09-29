from django import forms
from django.contrib.auth.models import User
from .models import Product, Return
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']
class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['product', 'reason']