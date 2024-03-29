from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos/", include("todo.urls")),
    path("authors/", include("author.urls")),
    path("books/", include("book.urls")),
    path("abc/", include("news.urls")),
    path("users/", include("user.urls"))
]