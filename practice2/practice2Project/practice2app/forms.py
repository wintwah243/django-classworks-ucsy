from django import forms

from .models import Practice2


class Practice2Form(forms.ModelForm):
    class Meta:
        model = Practice2
        fields = '__all__'