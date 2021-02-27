from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,mixins
from rest_framework import filters
from drfapp.models import Product
from drfapp.serializers import ProductSerializer


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   # 关联序列化类
    # 添加过滤器后端支持类，搜索过滤器、排序过滤器
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    search_fields = ("name","price")    # 指定搜索字段
    ordering_fields = ("price",)   # 指定搜索字段