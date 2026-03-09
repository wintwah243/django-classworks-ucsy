from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
    expiry_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name