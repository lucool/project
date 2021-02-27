from django.db import models


class Emp(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    salary = models.FloatField()
    manager = models.ForeignKey('self',on_delete=models.CASCADE,null=True)  # 外键自关联

    class Meta:
        db_table = "emps"