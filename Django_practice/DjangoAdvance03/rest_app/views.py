from rest_framework import viewsets,mixins

from rest_app.models import Article
from rest_app.serializers import ArticleSerializer


class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                     mixins.CreateModelMixin,mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,mixins.UpdateModelMixin):  # 自定义视图集类
    queryset = Article.objects.all()   # 重写queryset类属性
    serializer_class = ArticleSerializer   # 关联序列化类
