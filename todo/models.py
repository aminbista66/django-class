from django.db import models
from user.models import User

class Todo(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    completed = models.BooleanField(default=False)
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
