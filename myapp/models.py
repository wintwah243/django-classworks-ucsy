from django.db import models

class Student(models.Model):
      name = models.CharField(max_length=30)
      dob = models.DateField()
      contact = models.IntegerField()
      email = models.CharField(max_length=30)

      def __str__(self):
        return self.name
