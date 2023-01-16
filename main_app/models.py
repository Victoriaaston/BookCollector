from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=75)
    genre = models.CharField(max_length=75)
    description = models.TextField(max_length=250)
    author = models.CharField(max_length=75)

    def __str__(self):
        return self.name