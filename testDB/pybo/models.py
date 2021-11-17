from django.db import models

# Create your models here.

class MallBoard(models.Model):
    name = models.TextField(max_length=255)
    job = models.IntegerField(max_length=255)
    age = models.IntegerField()
    mySelf = models.TextField(max_length=255)