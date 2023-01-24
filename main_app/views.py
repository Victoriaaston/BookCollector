from django.shortcuts import render, redirect

from .models import Book, Opinion

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import RatingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    id_list = book.opinions.all().values_list('id')
    opinions_book_doesnt_have = Opinion.objects.exclude(id__in=id_list)
    rating_form = RatingForm()
    return render(request, 'books/detail.html', { 'book': book, 
    'rating_form': rating_form,
    'opinions': opinions_book_doesnt_have
     })

def add_rating(request, book_id):
    form = RatingForm(request.POST)
    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.book_id = book_id
        new_rating.save()
        return redirect('detail', book_id=book_id)
    
def assoc_opinion(request, book_id, opinion_id):
    Book.objects.get(id=book_id).opinions.add(opinion_id)
    return redirect ('detail', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    #success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    fields = ['description']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

class OpinionList(ListView):
  model = Opinion

class OpinionDetail(DetailView):
  model = Opinion

class OpinionCreate(CreateView):
  model = Opinion
  fields = '__all__'

class OpinionUpdate(UpdateView):
  model = Opinion
  fields = ['name', 'color']

class OpinionDelete(DeleteView):
  model = Opinion
  success_url = '/toys/'