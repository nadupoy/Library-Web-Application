from django.shortcuts import render

from .models import Book


def home_page(request):
    return render(request, 'library_app/index.html')


def library_page(request):
    books = Book.objects.all()
    context = {
        'books': books,
        }
    return render(request, 'library_app/library.html', context)


def book_details_page(request, book_title):
    book = Book.objects.get(title=book_title)
    context = {
        'book': book,
    } 
    return render(request, 'library_app/details.html', context)