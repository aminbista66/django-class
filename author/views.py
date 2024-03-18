from django.shortcuts import HttpResponse
from .models import Author


def author_view(request):
    # authors = Author.objects.filter(first_name__iexact="jhon")
    # authors = Author.objects.filter(first_name__icontains="Jhon")
    authors = Author.objects.filter(created_at__range=[18, 25])
    print("\n")
    print(authors)
    print("\n")
    return HttpResponse("Hello World")