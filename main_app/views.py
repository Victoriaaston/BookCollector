from django.shortcuts import render

from django.http import HttpResponse

#fake data for now
# Add the Cat class & list and view function below the imports
class Book:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, genre, description, author):
    self.name = name
    self.genre = genre
    self.description = description
    self.author = author

books = [
  Book('Brain Food', 'Non-Fiction', 'Informative book about the foods we eat and how they affect our brain', "Lisa Mosconi"),
  Book('Silence', 'Y/A fiction', 'Classic romance with a mystery twist', "Natasha Preston"),
  Book('Midnight Sun', 'Y/A fiction', 'fictional spinoff of a previous series', "Stephenie Meyer")
]


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    return render(request, 'books/index.html', {'books': books})