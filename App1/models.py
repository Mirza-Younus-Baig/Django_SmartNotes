from django.db import models

# Create your models here.

class AppInfo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    userId = models.IntegerField()
    createdOn = models.DateTimeField(auto_created=True)