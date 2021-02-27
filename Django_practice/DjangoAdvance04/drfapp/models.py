from django.db import models


class Product(models.Model):   # 产品模型
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    class Meta:
        db_table = "products"


class Book(models.Model):   # 书本模型
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    class Meta:
        db_table = "books"


class Toy(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    class Meta:
        db_table = "toys"