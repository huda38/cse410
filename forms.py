from django import forms
from .models import Admission
from .models import Contact


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['name', 'email', 'dob', 'mobile_number', 'city', 'address', 'gender', 'appiled_for']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']