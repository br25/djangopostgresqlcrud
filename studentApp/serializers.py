from rest_framework import serializers 
from studentApp.models import Student, Course
 
 
class StudentAppSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Student
        fields = ('id',
                  'firstname',
                  'lastname',
                  'email',
                  'courseid')

    class Metatwo:
        model = Course
        fields = ('id',
                  'coursename',
                  'price')
