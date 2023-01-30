from turtle import mode
from django.db import models
class Emps(models.Model):
    name=models.CharField(max_length=20)
    sal=models.IntegerField()
    def __str__(self):
        return self.name
class Temp(models.Model):
    uid=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,unique=True)
    dob=models.DateField(auto_now=False)
    times=models.TimeField(auto_now=False)
    dttime=models.DateTimeField(auto_now=False)
    img=models.ImageField(upload_to='pics')
    address=models.TextField()
    def __str__(self) -> str:
        return self.name
class Language(models.Model):
    name=models.CharField(max_length=20)
    duration=models.CharField(max_length=30)
    fees=models.IntegerField()
    trainer=models.CharField(max_length=20)
    image=models.ImageField(upload_to='pics')
    def __str__(self) -> str:
        return self.name
class ProgrammingCourse(models.Model):
    name=models.CharField(max_length=20)
    duration=models.CharField(max_length=30)
    fees=models.IntegerField()
    trainer=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name 