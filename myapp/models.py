from django.db import models
from django.core.exceptions import ValidationError

class Student(models.Model):
      name = models.CharField(max_length=30)
      dob = models.DateField()
      contact = models.IntegerField()
      email = models.CharField(max_length=30)

      def __str__(self):
        return self.name


def default_city():
    return "San Diego"

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=30, default=default_city)
    state = models.CharField(max_length=2, default='CA')

    def __str__(self):
        return self.name

class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class StudentDetail(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter your full name as per official records",
    )
    age = models.IntegerField(
        help_text="Age mush be 18 or above",
    )

def StartsWithAValidator(value):
    if not value.startswith('A'):
        raise ValidationError('Must start with "A"')


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[StartsWithAValidator],
    )

def clean(self):
    if self.city == 'San Diego' and self.state != 'CA':
        raise ValidationError('Wait San Diego is CA!, are you sure there is another San Diego in %s ?' % self.state)
