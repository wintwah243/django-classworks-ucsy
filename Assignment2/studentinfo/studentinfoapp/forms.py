from django import forms
from datetime import date

INTEREST_DICT = {
    'KE': 'Knowledge Engineering',
    'SE': 'Software Engineering',
    'CSF': 'Cyber Security and Forensics',
    'BIS': 'Business Information Systems',
    'HPC': 'High Performance Computing',
    'ES': 'Embedded Systems',
    'CCN': 'Computer Communication and Networks',
}

SEMESTER_DICT = {
    'IV': 'Semester IV',
    'V': 'Semester V',
    'VI': 'Semester VI',
}

INTEREST_CHOICES = [
    ('KE', 'Knowledge Engineering'),
    ('SE', 'Software Engineering'),
    ('CSF', 'Cyber Security and Forensics'),
    ('BIS', 'Business Information Systems'),
    ('HPC', 'High Performance Computing'),
    ('ES', 'Embedded Systems'),
    ('CCN', 'Computer Communication and Networks'),
]

SEMESTER_CHOICES = [
    ('1', 'Semester IV'),
    ('2', 'Semester V'),
    ('3', 'Semester VI'),
]

class StudentForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@ucsy.edu.mm'}))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1995, date.today().year + 1)))
    interests = forms.MultipleChoiceField(choices=INTEREST_CHOICES,widget=forms.CheckboxSelectMultiple)
    academic_year = forms.ChoiceField(choices=SEMESTER_CHOICES,widget=forms.RadioSelect)
