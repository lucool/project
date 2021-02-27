from django.db import models


class Member(models.Model):   # 成员多方模型
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)

    class Meta:
        db_table = "members"


class Community(models.Model):   # 社团多方模型
    name = models.CharField(max_length=20)
    buildtime = models.DateField()
    members = models.ManyToManyField(Member,through="Relation",related_name="comms")  # 分别关联Member多方模型、中间关系模型Relation

    class Meta:
        db_table = "communities"


class Relation(models.Model):   # "第三方关系模型"
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    community = models.ForeignKey(Community,on_delete=models.CASCADE)
    join_reason = models.CharField(max_length=30,null=True)

    class Meta:
        db_table = "relations"