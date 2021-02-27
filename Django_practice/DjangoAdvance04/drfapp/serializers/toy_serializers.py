from rest_framework import serializers

from drfapp.models import Toy


class ToySerializer(serializers.ModelSerializer):  # 产品序列化类

    class Meta:
        model = Toy
        fields = ["id","name","price"]