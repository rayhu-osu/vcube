from django.db import models
from vip.models import Item
from sign_up.models import Consumer
from valet.models import Driver

class Cart(models.Model):

    # 1 user only has exact 1 cart
    id = models.AutoField(primary_key=True)
    consumer = models.OneToOneField(Consumer, on_delete=models.PROTECT)
    # item = models.ManyToManyField(Item)

    def __str__(self):
        return str(self.consumer)

# Gradually by-pass Cart, A cart's view consists of many orders.
class Order(models.Model):

    id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.PROTECT)
    item = models.ManyToManyField(Item)
    date = models.DateTimeField(auto_now=True)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, blank=True, null=True)
    processed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + '-' + str(self.consumer) + '-' + str(self.date)
