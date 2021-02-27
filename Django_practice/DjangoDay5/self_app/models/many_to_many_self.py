from django.db import models


class WeiUser(models.Model):
    username = models.CharField(max_length=20)

    class Meta:
        db_table = "weiusers"


class Relation(models.Model):
    followed = models.ForeignKey(WeiUser,on_delete=models.CASCADE,related_name="followd_relations")
    fans = models.ForeignKey(WeiUser,on_delete=models.CASCADE,related_name="fans_relations")

    class Meta:
        db_table = "wei_relations"