from django.db import models

# Create your models here.

class Table(models.Model):
    date = models.DateTimeField()
    text = models.TextField()
