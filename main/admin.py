from django.contrib import admin
from .models import Book, Car, Phone, Student, Teacher

# Register your models here.

admin.site.register(Book)
admin.site.register(Car)
admin.site.register(Phone)
admin.site.register(Student)
admin.site.register(Teacher)