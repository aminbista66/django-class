from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    completed = models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=250, null=False, blank=False, default="low")

    def __str__(self):
        return self.title


