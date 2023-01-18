from django.db import models

from django.urls import reverse

STARS = (
    ("1", "1 Star"),
    ("2", "2 Stars"),
    ("3", "3 Stars"),
    ("4", "4 Stars"),
    ("5", "5 Stars")
)

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
    
class Rating(models.Model):
    date = models.DateField('rating date')
    star = models.CharField(
        max_length=1, 
        choices=STARS,
        default=[4][0]
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_star_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']