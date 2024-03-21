from django.urls import path
from .views import list_articles

urlpatterns = [
    path("", list_articles)
]