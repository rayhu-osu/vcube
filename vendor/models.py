from django.db import models


class Store(models.Model):

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img/')
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length=30)
    street = models.CharField(max_length = 100, blank=True)
    city = models.CharField(max_length = 40, blank=True)
    state = models.CharField(max_length = 2, blank=True)
    zip_code= models.CharField(max_length = 5, blank=True)

    def __str__(self):
        return str(self.id) + '-' + self.name
