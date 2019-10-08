from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    school = models.ForeignKey('school.School', related_name='students', on_delete=models.CASCADE)
    is_adult = models.BooleanField(default=False)

    def __str__(self):
        return self.name