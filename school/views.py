
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from school import models
from . import serializers


class SchoolView(APIView):
    def get(self, request, pk=None):
        if pk:
            schools = get_object_or_404(models.School.objects.all(), pk=pk)
            serializer = serializers.SchoolSerializer(schools)
            return Response({"school": serializer.data})
        schools = models.School.objects.all()
        serializer = serializers.SchoolSerializer(schools, many=True)
        return Response({"schools": serializer.data})

    def post(self, request, pk=None):
        school = request.data.get('school')
        serializer = serializers.SchoolSerializer(data=school)
        print(school)
        if serializer.is_valid(raise_exception=True):
            school_saved = serializer.save()
        return Response({"success": "School '{}' created successfully".format(school_saved.name)})

    def put(self, request, pk):
        saved_school = get_object_or_404(models.School.objects.all(), pk=pk)
        data = request.data.get('school')
        serializer = serializers.SchoolSerializer(instance=saved_school, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_school = serializer.save()
        return Response({"success": "School '{}' updated successfully".format(saved_school.name)})

    def delete(self, request, pk):
        # Get object with this pk
        school = get_object_or_404(models.School.objects.all(), pk=pk)
        school.delete()
        return Response({"message": "School with id `{}` has been deleted.".format(pk)}, status=204)


class StudentRegistrationView(APIView):
    def put(self, request, pk):
        saved_school = get_object_or_404(models.School.objects.all(), pk=pk)
        student_id = request.data.get('student_id')
        serializer = serializers.StudentRegisterSerializer(instance=saved_school, data={"student_id":student_id}, partial=True)
        if serializer.is_valid(raise_exception=True):
            school_saved = serializer.save()
        return Response({"success": "Student '{}' registered to School {} successfully".format(student_id, school_saved.name)})


class StudentsListView(generics.ListAPIView):

    def get(self, request, pk=None):
        school = get_object_or_404(models.School.objects.all(), pk=pk)
        self.queryset = models.School.objects.filter(id=school.id)
        serializer = serializers.StudentsListSerializer(self.queryset, many=True, context={'request': request})
        page = self.paginate_queryset(serializer.data[0].get('students'))
        return self.get_paginated_response(page)