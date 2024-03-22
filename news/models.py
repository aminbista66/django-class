from django.db import models
from user.models import User

class Article(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    like = models.ManyToManyField(User, blank=True, related_name="articles_likes")

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=250, null=False, blank=False) # what is written
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # which article is commented
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE) # who commented

    def __str__(self):
        return f"{self.commented_by.username} commented on {self.article.title}"