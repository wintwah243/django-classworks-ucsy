from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name