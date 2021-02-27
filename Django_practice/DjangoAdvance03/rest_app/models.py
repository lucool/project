from django.db import models


class Article(models.Model):   # 文章模型
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)

    class Meta:
        db_table = "articles"