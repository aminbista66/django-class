from django.http import JsonResponse
from .models import Book


def book_view(request):
    books = Book.objects.filter(author__first_name__iexact="jhon")
    response_data = []

    for book in books:
        response_data.append(
            {
                "title": book.title,
                "author": {
                    "first_name": book.author.first_name,
                    "last_name": book.author.last_name,
                    "age": book.author.age,
                },
            }
        )
    return JsonResponse(response_data, safe=False)