from django.db import models
from django.db.models import Manager


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    score = models.FloatField()

    class Meta:
        db_table = "students"


class CakeManager(Manager):   #  继承了Manager的类，即为模型对象管理器的类

    def create_cake(self,cake_name,cake_price,cake_color):
        new_cake = self.model()   # 创建对象管理器所在的模型对象
        new_cake.name = cake_name
        new_cake.price = cake_price
        new_cake.color = cake_color
        new_cake.save()
        return new_cake


class Cake(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    color = models.CharField(max_length=20)
    manager = CakeManager()   #  将manager类属性设置为自定义的对象管理器

    class Meta:
        db_table = "cakes"
