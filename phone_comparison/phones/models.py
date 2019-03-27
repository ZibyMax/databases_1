from django.db import models

# Create your models here.


class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    memory = models.IntegerField()
    display = models.FloatField()
