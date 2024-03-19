from django.db import models
from author.models import Author


class Book(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Book2(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title