from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()

    def __str__(self):
        return self.name


class StorePermission(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    class Meta:
        default_permissions = ('add', )
        permissions = (('give refund', 'Can refund customers'),('can hire', 'Can hire employees'))