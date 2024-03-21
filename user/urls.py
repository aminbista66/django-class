from django.urls import path
from .views import user_lists

urlpatterns = [
    path("", user_lists)
]