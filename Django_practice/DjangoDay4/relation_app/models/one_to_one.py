from django.db import models


class Person(models.Model):  # 人模型，“一”方
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)

    class Meta:
        db_table = "person"


class Card(models.Model):   # 身份证模型，“一”方
    cardno = models.CharField(max_length=20,unique=True)
    color = models.CharField(max_length=20)
    per = models.OneToOneField(Person,related_name="c",on_delete=models.CASCADE)  # 关联Person类

    class Meta:
        db_table = "cards"
