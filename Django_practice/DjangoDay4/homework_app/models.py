from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.FloatField()

    class Meta:
        db_table = "workers"