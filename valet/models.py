from django.db import models
from vendor.models import Store


class Driver(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=40, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id) + ' - ' + self.username

# StoreSequence = the store_ids according to the order a driver should visit, separated by single space.
class StoreSequence(models.Model):

    id = models.AutoField(primary_key=True)
    seq = models.CharField(max_length=200)
    driver = models.OneToOneField(Driver, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.seq

# ConsumerSequence stores the consumer_ids according to the order a driver should visit, separated by single space.
class ConsumerSequence(models.Model):

    id = models.AutoField(primary_key=True)
    seq = models.CharField(max_length=200)
    driver = models.OneToOneField(Driver, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.seq
