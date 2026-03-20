from django import forms

from .models import Practice1


class Practice1Form(forms.ModelForm):
    class Meta:
        model = Practice1
        fields = ['name', 'email']