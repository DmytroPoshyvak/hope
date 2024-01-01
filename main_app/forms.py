from django import forms

class CheckOutForm(forms.Form):
    name = forms.CharField(required=True)
    phon = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    session_key = forms.CharField(required=True)