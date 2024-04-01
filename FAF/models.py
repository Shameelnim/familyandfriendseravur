from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to='media',default='book.jpg',blank=True)
    body = models.TextField()
    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
class Speech(models.Model):
    image=models.ImageField(upload_to='media',default='book.jpg',blank=True)
    name = models.CharField(max_length=200,default="")
    body = models.TextField()



class MainCourse(models.Model):
    name = models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to='media',default='book.jpg',blank=True)
    body = models.TextField()
    def __str__(self) -> str:
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name