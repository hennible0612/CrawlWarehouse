from django.db import models
from adaptor.model import CsvModel
from adaptor.fields import CharField, IntegerField, BooleanField

# Create your models here.

class MallBoard(models.Model):
    name = models.TextField(max_length=255)
    job = models.TextField(max_length=255)
    age = models.IntegerField()
    mySelf = models.TextField(max_length=255)

    def __str__(self):
        return self.name
