from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    credit_hours = models.IntegerField(max_length=20)
    syllabus = models.FileField()

    def __str__(self):
        return self.course_title


class Section(models.Model):
    name = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.name


class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='students')
    first_name= models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    year_of_enrollment = models.DateField()
    photo = models.ImageField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Test(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='test')
    name = models.CharField(max_length=30)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=1000)
    timer = models.DurationField()

    def __str__(self):
        return self.name


class Club(models.Model):
    club_name = models.CharField(max_length=20)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.club_name
