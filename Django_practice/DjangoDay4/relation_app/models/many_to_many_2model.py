from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "users"


class Group(models.Model):
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(User,related_name="groups")  # 关联用户模型

    class Meta:
        db_table = "groups"