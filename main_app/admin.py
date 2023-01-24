from django.contrib import admin

from .models import Book, Rating, Opinion
# Register your models here.
admin.site.register(Book)

admin.site.register(Rating)

admin.site.register(Opinion)