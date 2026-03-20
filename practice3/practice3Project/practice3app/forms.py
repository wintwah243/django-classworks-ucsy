from django import forms

from .models import Practice3


class Practice3Form(forms.ModelForm):
    class Meta:
        model = Practice3
        fields = "__all__"