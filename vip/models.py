from django.db import models
from vendor.models import Store

class Category(models.Model):
    BEAUTY = 'Beauty and Health'
    CLOTHING = 'Clothing'
    ELECTRONIC = 'Electronics'
    FOOD = 'Food and Drinks'
    GROCERY = 'Grocery'
    HOME = 'Home'

    CATEGORY_CHOICES = (
            (BEAUTY, 'Beauty and Health'), (CLOTHING, 'Clothing'),
            (ELECTRONIC, 'Electronics'), (FOOD,'Food and Drinks'),
            (GROCERY, 'Grocery'), (HOME, 'Home'),
    )
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name


class Item (models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length = 100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT) # key
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ManyToManyField(Store) # key
    description = models.CharField(max_length = 2000, blank=True)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return self.name + "- $" + str(self.price)

