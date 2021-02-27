from django.db import models


class School(models.Model):   # 一方
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = "schools"


class Student(models.Model):   # 多方
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    score = models.FloatField()
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="students")  # 外键类属性

    class Meta:
        db_table = "students"