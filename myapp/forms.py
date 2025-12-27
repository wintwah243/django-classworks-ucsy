from django import forms

class StudentForm(forms.Form):
    username = forms.CharField(label='Enter your name', max_length=100)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Enter your email', max_length=100)