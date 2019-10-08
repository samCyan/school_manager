
from django.db import models

schools_boards = (('CBSE','CBSE'), ('CBSE','ICIC'))

class School(models.Model):
    name = models.CharField(max_length=200)
    board = models.CharField(choices=schools_boards, max_length=100)

    def __str__(self):
        return self.name