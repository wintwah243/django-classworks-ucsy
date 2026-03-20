from django import forms
from .models import Practice5


class Practice5Form(forms.ModelForm):
    class Meta:
        model = Practice5
        fields = ['name','email']