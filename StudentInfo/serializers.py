from rest_framework import serializers

from StudentInfo.models import Student, Section, Course, Test, Club


class StudentSerealizer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class SectionSerealizer(serializers.ModelSerializer):


    class Meta:
        model = Section
        fields = '__all__'


class CourseSerealizer(serializers.ModelSerializer):


    class Meta:
        model = Course
        fields = '__all__'


class TestSerealizer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'

class ClubSerealizer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'