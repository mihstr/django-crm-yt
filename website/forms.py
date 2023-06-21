from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Email address"
    }))
    first_name = forms.CharField(label="", max_length=40, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "First name"
    }))
    last_name = forms.CharField(label="", max_length=40, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Last name"
    }))
