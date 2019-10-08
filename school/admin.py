from django.contrib import admin

from .models import School

from student.models import Student

class StudentInline(admin.TabularInline):
    model = Student

class SchoolAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]
admin.site.register(School, SchoolAdmin)