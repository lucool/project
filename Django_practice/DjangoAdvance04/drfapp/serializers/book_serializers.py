from rest_framework import serializers

from drfapp.models import Book
from drfapp.util.error import MyException


class BookSerializer(serializers.ModelSerializer):   # 书本序列化类

    def validate(self, attrs):    # 重写validate()方法，指定逻辑验证规则
        print("validate()......")
        bookname = attrs.get("name")  # 获取接收到的书本名称
        if Book.objects.filter(name=bookname).exists():
            raise MyException("该书名称已经存在，不能重复添加！")
        return attrs

    class Meta:
        model = Book
        fields = ["url","name","price"]