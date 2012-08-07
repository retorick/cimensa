from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=255)
    part_of_speech = models.CharField(max_length=10)
    definition = models.CharField(max_length=500)
