from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_app.models import Fruit
from drf_app.serializers import FruitSerializer


@api_view(["GET","PUT","DELETE"])
def fruit_view(request,fruit_id):
    try:
        fruit = Fruit.objects.get(pk=fruit_id)
    except Fruit.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = FruitSerializer(fruit)   #  将查询到的水果对象封装到序列化对象中
        return Response(ser.data)   # 从序列化对象中获取拆分后的水果对象，以响应的方式发送到客户端
    elif request.method == "PUT":
        ser = FruitSerializer(fruit,data=request.data)   # 将“旧数据”与提交上来的“新数据”一起封装到序列化对象中
        if ser.is_valid():   #  验证客户端提交的数据是否有效
            ser.save()
            return Response(ser.data)
        else:   # 客户端提交的数据验证未通过
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        fruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)