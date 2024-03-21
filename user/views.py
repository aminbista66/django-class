from django.http import JsonResponse
from .models import User
from news.models import Article, Comment

# Create your views here.
def user_lists(request):
    db_users = User.objects.all()
    response_users = []

    for user in db_users:
        db_articles = Article.objects.filter(writer__pk=user.pk)
        articles = []

        for article in db_articles:
            db_comments = Comment.objects.filter(article__pk=article.pk)
            comments = []

            for comment in db_comments:
                comments.append(
                    {
                        "content": comment.content,
                        "commented_by": {
                            "first_name": comment.commented_by.first_name,
                            "last_name": comment.commented_by.last_name
                        }
                    }
                )

            articles.append(
                {
                    "title": article.title,
                    "content": article.content,
                    "published_at": article.published_at,
                    "comments": comments
                }
            )

        response_users.append(
            {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "articles": articles
            }
        )
    return JsonResponse(response_users, safe=False)