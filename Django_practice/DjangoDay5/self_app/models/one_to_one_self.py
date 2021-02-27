from django.db import models


class Spy(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    manager = models.OneToOneField('self',on_delete=models.CASCADE,null=True)   # 一对一自关联

    class Meta:
        db_table = "spies"
