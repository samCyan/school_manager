# api/serializers.py
from rest_framework import serializers
from school import models
from student.serializers import StudentSerializer
from student.models import Student
from django.db.models import Model

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'is_adult', 'age']



class SchoolSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'board',
            'students'
        )
        model = models.School

    def create(self, validated_data):
        students = validated_data.pop("students")
        print(validated_data)
        school = models.School.objects.create(**validated_data)
        for student in students:
            Student.objects.create(school=school, **student)
        return school


    def update(self, instance, validated_data, pk=None):
        students_data = validated_data.pop('students')
        students = (instance.students).all()
        students = list(students)
        instance.name = validated_data.get('name', instance.name)
        instance.board = validated_data.get('board', instance.board)
        instance.save()
        for student_data in students_data:
            student = students.pop(0)
            student.name = student_data.get('name', student.name)
            student.age = student_data.get('age', student.age)
            student.is_adult = student_data.get('is_adult', student.is_adult)
            student.save()
        return instance


class StudentRegisterSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField()
    class Meta:
        fields = (
            'student_id',)
        model = models.School

    def update(self, instance, validated_data, pk=None):
        student_id = validated_data.get('student_id')
        try:
            obj = Student.objects.get(id=student_id)
            obj.school = instance
            obj.save()
        except Model.DoesNotExist:
            pass
        return instance

class StudentsListSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    def get_students(self, obj):
        ordered_queryset = Student.objects.order_by("name").filter(school=obj)
        student_name = self.context['request'].query_params.get('name', None)
        if student_name:
            ordered_queryset = ordered_queryset.filter(name=student_name)
        student_age = self.context['request'].query_params.get('age', None)
        if student_age:
            ordered_queryset = ordered_queryset.filter(age=student_age)
        return StudentSerializer(ordered_queryset, many=True, context=self.context).data

    class Meta:
        fields = (
            'students',)
        model = models.School