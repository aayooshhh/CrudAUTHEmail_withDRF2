from django.db import models

# Create your models here.
class StudentM(models.Model):
    roll=models.IntegerField()
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    num=models.BigIntegerField()
    email=models.EmailField()
    dob=models.DateField()
