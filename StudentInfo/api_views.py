from rest_framework import viewsets
from . import models
from . import serializers

class CourseViewset(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerealizer

class TestViewset(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerealizer

class ClubViewset(viewsets.ModelViewSet):
    queryset = models.Club.objects.all()
    serializer_class = serializers.ClubSerealizer

class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerealizer


class SectionViewset(viewsets.ModelViewSet):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerealizer

