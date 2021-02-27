from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = "users"
