from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    score = models.FloatField()

    class Meta:
        db_table = "students"