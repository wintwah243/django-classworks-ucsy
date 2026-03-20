from django import forms
from .models import Practice4


class Practice4Form(forms.ModelForm):
    class Meta:
        model = Practice4
        fields = "__all__"