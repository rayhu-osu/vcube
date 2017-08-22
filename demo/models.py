from django.db import models


class Number (models.Model):

    number_1 = models.FloatField()
    number_2 = models.FloatField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id) + ' link'


