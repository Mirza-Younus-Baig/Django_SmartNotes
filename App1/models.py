from django.db import models
import datetime

# Create your models here.

class AppInfo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(default = "Enter description here")
    userId = models.IntegerField(serialize=True, unique=True)
    createdOn = models.DateTimeField(default=datetime.datetime.now)


class StudentInfo(models.Model):
    studentID = models.IntegerField(unique=True)
    name = models.TextField()
    section = models.CharField(max_length=2)


