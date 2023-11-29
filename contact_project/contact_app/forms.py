# contact_app/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    def clean_marital_status(self):
        marital_status = self.cleaned_data.get('marital_status')
        if marital_status not in ['s', 'd', 'm']:
            raise forms.ValidationError("Invalid marital status. Only 's', 'd', and 'm' are allowed.")
        return marital_status