from django import forms
from django.contrib.auth.models import User
from .models import Product, Return
<<<<<<< HEAD
=======

>>>>>>> 5ce74443ef94a5fc0bed329c0a606554a14677cf
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
<<<<<<< HEAD
=======

>>>>>>> 5ce74443ef94a5fc0bed329c0a606554a14677cf
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']
<<<<<<< HEAD
class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['product', 'reason']
=======

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['product', 'reason']
>>>>>>> 5ce74443ef94a5fc0bed329c0a606554a14677cf
