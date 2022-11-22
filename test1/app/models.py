from django.db import models

# Create your models here.
class Date(models.Model):
    date = models.CharField(max_length=5000)