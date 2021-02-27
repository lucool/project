from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    class Meta:
        db_table = "fruits"
