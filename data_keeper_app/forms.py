# from django.forms import ModelForm
# from .models import app_user
from django import forms
from django.core.validators import integer_validator

from django.forms import TextInput


class app_user(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    phone_number = forms.CharField(max_length=10, required=False,validators=[integer_validator.regex])
