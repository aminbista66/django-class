from django.shortcuts import HttpResponse

def author_view(request):

    return HttpResponse("Hello World")