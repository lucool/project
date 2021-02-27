import django_filters

from drfapp.models import Book


class BookFilter(django_filters.rest_framework.FilterSet):   # 自定义书本过滤器
    # 过滤器的类属性名将作为过滤参数名（查询字符串参数名）
    bname = django_filters.CharFilter(field_name="name",lookup_expr="contains")
    bprice = django_filters.NumberFilter(field_name="price",lookup_expr="gte")

    class Meta:
        model = Book
        fields = ["price","name"]   #  该fields中也可以添加模型类属性名