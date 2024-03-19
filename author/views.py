from django.shortcuts import HttpResponse
from .models import Author
from django.http import JsonResponse


def author_view(request):
    # authors = Author.objects.filter(first_name__iexact="jhon")
    # authors = Author.objects.filter(first_name__icontains="Jhon")

    authors = Author.objects.filter(created_at__range=[18, 25])
    
    total_author = authors.count() # return integer value
    is_exists = authors.exists() # return boolean value


    response_author = []

    for i in authors:
        response_author.append({
            "first_name": i.first_name,
            "last_name": i.last_name,
            "age": i.age,
        })
    return JsonResponse(response_author, safe=False)