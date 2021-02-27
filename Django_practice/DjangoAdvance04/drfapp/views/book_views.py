from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,mixins
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from drfapp.filters import BookFilter
from drfapp.models import Book
from drfapp.serializers import BookSerializer


class BookViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,mixins.UpdateModelMixin):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)   # 过滤器后端支持类必须添加
    filter_class = BookFilter   # 挂载自定义过滤器类

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        try:
            print("准备验证了......")
            result = ser.is_valid(raise_exception=True)  # 会触发格式验证与逻辑验证
        except APIException as e:
            data = {
                "code":"999",
                "msg":e.detail
            }
            return Response(data)
        ser.save()
        print("ser.data=",ser.data)
        return Response(ser.data)