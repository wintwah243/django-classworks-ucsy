from django import forms
from .models import Medicine

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'category', 'price', 'quantity', 'expiry_date', 'description']