from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from homework_app.models import Student
from homework_app.serializers import StudentSerializer


class StudentViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,mixins.CreateModelMixin,
                     mixins.UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:   # 没有查出学生记录
            data = {
                "code":"900",
                "msg":"没有这条数据！",
            }
            return Response(data)
        ser = self.get_serializer(instance)
        return Response(ser.data)

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        try:
            ser.is_valid(raise_exception=True)
        except APIException as e:
            result = {
                "code":"902",
                "msg":"创建失败！",
            }
            return Response(result)
        ser.save()
        headers = self.get_success_headers(ser.data)
        return Response(ser.data, status=status.HTTP_201_CREATED, headers=headers)