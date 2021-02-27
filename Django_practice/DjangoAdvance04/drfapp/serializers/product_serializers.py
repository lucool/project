from rest_framework import serializers

from drfapp.models import Product

class ProductSerializer(serializers.ModelSerializer):  # 产品序列化类

    class Meta:
        model = Product
        fields = ["url","name","price"]