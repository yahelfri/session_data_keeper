from django import forms


class app_user(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    phone_number = forms.CharField(max_length=10, required=False)
