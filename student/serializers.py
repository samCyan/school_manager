
from rest_framework import serializers
from student import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'age',
            'is_adult',
            'school'
        )
        model = models.Student
    school = serializers.ReadOnlyField(source='school.name')
