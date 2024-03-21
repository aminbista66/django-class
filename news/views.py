from django.http import JsonResponse
from .models import Article, Comment


def list_articles(request):
    # db_articles = Article.objects.filter(writer__pk=userId)    get userId from url
    
    db_articles = Article.objects.all()
    response_articles = []

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
        
        response_articles.append(
            {
                "title": article.title,
                "content": article.content,
                "published_at": article.published_at,
                "writer": {
                    "first_name": article.writer.first_name, # type:ignore
                    "last_name": article.writer.last_name # type:ignore
                },
                "comments": comments
            }
        )
    

    return JsonResponse(response_articles, safe=False)
