from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

def __str__(self) -> str:
    return self.fristname   

