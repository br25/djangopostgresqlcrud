from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    courseid = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname


class Course(models.Model):
    coursename = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    