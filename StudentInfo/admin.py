from django.contrib import admin
from .models import Student,Test,Course, Club, Section
# Register your models here.
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Club)
admin.site.register(Course)
admin.site.register(Section)