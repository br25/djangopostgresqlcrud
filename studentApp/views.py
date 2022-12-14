
from django.shortcuts import render
from .models import Student
from rest_framework import generics
from .serializers import StudentAppSerializer

class StudentCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Student.objects.all(),
    serializer_class = StudentAppSerializer


class StudentList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Student.objects.all()
    serializer_class = StudentAppSerializer


...
class StudentDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Student.objects.all()
    serializer_class = StudentAppSerializer


...
class StudentUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Student.objects.all()
    serializer_class = StudentAppSerializer


class StudentDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Student.objects.all()
    serializer_class = StudentAppSerializer


