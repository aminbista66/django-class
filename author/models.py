from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    age = models.IntegerField(default=18)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"