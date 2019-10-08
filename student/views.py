from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from student import models
from . import serializers


class StudentList(APIView):
    def perform_create(self, serializer):
        serializer.save(school=self.request.school)
    def get(self, request, pk=None):
        students = models.Student.objects.all()
        serializer = serializers.StudentSerializer(students, many=True)
        return Response({"Students": serializer.data})

    def post(self, request):
        student = request.data.get('student')
        serializer = serializers.StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response({"success": "Student '{}' created successfully".format(student_saved.name)})

class StudentDetail(APIView):
    def get(self, request, pk):
        students = get_object_or_404(models.Student.objects.all(), pk=pk)
        serializer = serializers.StudentSerializer(students)
        return Response({"Student": serializer.data})

    def put(self, request, pk):
        saved_student = get_object_or_404(models.Student.objects.all(), pk=pk)
        data = request.data.get('student')
        serializer = serializers.StudentSerializer(instance=saved_student, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_student = serializer.save()
        return Response({"success": "Student '{}' updated successfully".format(saved_student.name)})

    def delete(self, request, pk):
        # Get object with this pk
        student = get_object_or_404(models.Student.objects.all(), pk=pk)
        student.delete()
        return Response({"message": "Student with id `{}` has been deleted.".format(pk)}, status=204)