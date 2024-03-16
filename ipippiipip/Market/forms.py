from django import forms
from .models import *

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class userform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class Admin(forms.ModelForm):
    class Meta:
        model = Admins
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']







            
            
            
            
            
            
            
            
            
            
            
            







































































