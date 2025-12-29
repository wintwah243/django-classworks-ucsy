from django import forms

class StudentForm(forms.Form):
    username = forms.CharField(label='Enter your name', max_length=100)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Enter your email', max_length=100)


class LoginForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=100)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)