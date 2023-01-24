from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_rating/', views.add_rating, name='add_rating'),
    path('opinions/', views.OpinionList.as_view(), name='opinions_index'),
    path('opinions/<int:pk>/', views.OpinionDetail.as_view(), name='opinions_detail'),
    path('opinions/create/', views.OpinionCreate.as_view(), name='opinions_create'),
    path('opinions/<int:pk>/update/', views.OpinionUpdate.as_view(), name='opinions_update'),
    path('opinions/<int:pk>/delete/', views.OpinionDelete.as_view(), name='opinions_delete'),
    path('books/<int:book_id>/assoc_opinion/<int:opinion_id>/', views.assoc_opinion, name='assoc_opinion'),
]