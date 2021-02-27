from rest_framework import serializers

from rest_app.models import Article


class ArticleSerializer(serializers.ModelSerializer):   # 自定义序列化类

    class Meta:
        model = Article    # 绑定的模型
        fields = ["url","title","desc"]   #  可以操作和显示的字段