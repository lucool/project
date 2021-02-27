from django.db import models


class Student(models.Model):    # 自定义模型类，对应于数据库表
    name = models.CharField(max_length=20)   # 模型类属性，对应于表中的字段
    sex = models.CharField(max_length=10)
    score = models.FloatField()

    class Meta:    # 内部元类
        db_table = "students"   #  指定映射到的表名称
