from django.db import models

from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=75)
    genre = models.CharField(max_length=75)
    description = models.TextField(max_length=250)
    author = models.CharField(max_length=75)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id':self.id})