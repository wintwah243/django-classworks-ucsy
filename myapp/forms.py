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

def validate_comment_word_count(value):
    count = len(value.split())
    if count < 30:
        raise forms.ValidationError(
            "Please enter a number between 3 and 100",
            params={'count': count}
        )

class ContactForm1(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='Enter your email')
    comment = forms.CharField(widget=forms.Textarea, validators=[validate_comment_word_count])

class Registration(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm your password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Enter your email')
    agree = forms.BooleanField(label='Do you agree to the terms and conditions?')

BIRTH_YEAR_CHOICES = ["1980", "1990", "1999", "2000", "2001"]
FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("red", "Red"),
    ("yellow", "Yellow"),
]
CHOICES = [("1", "First"), ("2", "Second")]

class SelectionForm(forms.Form):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_color = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)