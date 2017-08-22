from django.db import models
from valet.models import Driver


class Consumer(models.Model):

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

