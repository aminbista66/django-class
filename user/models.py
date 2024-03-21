from django.db import models


class User(models.Model):
    username = models.CharField(max_length=250, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    age = models.IntegerField()

    def __str__(self):
        return self.username