from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    form = models.CharField(max_length=200)
