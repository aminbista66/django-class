from django.urls import path
from .views import list_todo, retrieve_todo, update_todo

urlpatterns = [
    path("", list_todo),
    path("<int:todoId>/", retrieve_todo),
    path("<int:todoId>/update/", update_todo)
]