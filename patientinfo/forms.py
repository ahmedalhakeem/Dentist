from django import forms
from django.forms import ModelForm
from patientinfo.models import User

class Login_admin(forms.Form):
    username= forms.CharField(label="Username", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Username"}))
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}))

class Add_Patient(forms.Form):
    male = "m"
    female = "f"
    gender_type = [
        (male, "m"),
        (female, "f")
    ]
    name = forms.CharField(label="Full Name", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Patient's name"}))
    age = forms.CharField(label="Age", required=False, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Patient's age"}))
    gender = forms.ChoiceField(label="Gender",choices=gender_type, widget=forms.Select(attrs={"class": "form-control",}))
    contact = forms.CharField(label="Contact number", required=True, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Patient's contact number"}))

class Add_appointment(forms.Form):
    pass

