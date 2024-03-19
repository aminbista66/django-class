from django.shortcuts import HttpResponse
from .models import Book, Book2

def book_view(request):
    books = Book.objects.filter(author__first_name__iexact="jhon")
    print("\n")
    print(books)
    print("\n")
    return HttpResponse("Hello, World!")