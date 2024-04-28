from .models import Family
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Family


class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    contact_info = forms.CharField(max_length=100)
    emerg_contact = forms.CharField(max_length=100)

    class Meta:
        model = Family  # Update if using a custom User model
        
        fields = ('username', 'email', 'name', 'address', 'contact_info', 'emerg_contact')

class LoginForm(AuthenticationForm):
    class Meta:
        model = Family
        fields = ('username', 'password')