from rest_framework import serializers

from homework_app.models import Student
from homework_app.util.error import HomeException


class StudentSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        score = attrs.get("score")
        if score > 100 or score < 0:
            raise HomeException("成绩不符合要求！")
        return attrs

    class Meta:
        model = Student
        fields = ["url","name","sex","score"]