from rest_framework import serializers

from drf_app.models import Fruit


class FruitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fruit
        fields = ["id","name","price"]