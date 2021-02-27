from django.db import models


class School(models.Model):    #  "一"方模型
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    history = models.TextField(null=True)

    class Meta:
        db_table = "schools"


class Student(models.Model):   # "多"方模型
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    score = models.FloatField()
    school = models.ForeignKey(School,related_name="allstudents",on_delete=models.CASCADE)  # 外键类属性
    #school = models.ForeignKey(School,on_delete=models.CASCADE)  # 外键类属性

    class Meta:
        db_table = "stus"



