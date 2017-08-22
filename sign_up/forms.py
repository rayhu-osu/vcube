from django.forms import ModelForm
from .models import Consumer
from vendor.models import Store
from django import forms

# this creates a HTML form.
class ConsumerForm(ModelForm):
    
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    class Meta:
        model = Consumer
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'street',
                  'city', 'state', 'zip_code']

class StoreForm(ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    class Meta:
        model = Store
        fields = ['name', 'street', 'city', 'state', 'zip_code']

class LoginForm(ModelForm):
    TYPE_CHOICES= (
            ('VIP','VIP'),
            ('Vendor','Vendor'),
            ('Valet','Valet'),
            )
    user_type = forms.ChoiceField(widget=forms.Select, choices=TYPE_CHOICES, label='User Type')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    class Meta:
        model = Consumer
        fields = ['username']