from django.db import models

# Create your models here.

class Subject(models.Model):
    subID = models.CharField(max_length=10)
    subName = models.CharField(max_length=100)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.subID} ({self.subName})"

class Student(models.Model):
    sID = models.IntegerField()
    sName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sName}"

class Apply(models.Model):
    sApply = models.CharField(max_length=10)
    sID = models.ForeignKey("subjects.Student", on_delete=models.CASCADE) 
    subID = models.ForeignKey("subjects.Subject", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subID}: {self.sApply}"
    