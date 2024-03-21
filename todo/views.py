from django.http import JsonResponse
from .models import Todo, Tag


def list_todo(request):
    db_todos = Todo.objects.all()

    response_todo = []

    for todo in db_todos:
        db_tags = Tag.objects.filter(todo__pk=todo.pk)
        tags = []
        for tag in db_tags:
            tags.append(tag.name)
            
        response_todo.append(
            {
                "title": todo.title,
                "completed": todo.completed,
                "created_at": todo.created_at,
                "user": {
                    "username": todo.user.username,
                    "first_name": todo.user.first_name,
                    "last_name": todo.user.last_name,
                },
                "tags": tags,
            }
        )

    return JsonResponse(response_todo, safe=False)


def retrieve_todo(request, todoId):
    todo = Todo.objects.get(id=todoId)

    return JsonResponse(
        {
            "title": todo.title,
            "completed": todo.completed,
            "created_at": todo.created_at,
        },
        safe=False,
    )


def update_todo(request, todoId):
    todo = Todo.objects.get(id=todoId)

    todo.completed = True
    todo.save()

    return JsonResponse(
        {
            "title": todo.title,
            "completed": todo.completed,
            "created_at": todo.created_at,
        },
        safe=False,
    )


def delete_todo(request, todoId):
    todo = Todo.objects.get(id=todoId)

    todo.delete()

    return JsonResponse(
        {"message": "todo deleted successfully"},
        safe=False,
    )
