from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=20,verbose_name="水果名称")
    color = models.CharField(max_length=20,verbose_name="水果颜色")
    price = models.FloatField(verbose_name="价格")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "fruits"
        verbose_name = "水果模型"
        verbose_name_plural = verbose_name  # 后台管理显示的模型名称