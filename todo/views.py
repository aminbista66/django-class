from django.http import JsonResponse
from .models import Todo


def list_todo(request):
    db_todos = Todo.objects.all()

    response_todo = []

    for i in db_todos:
        response_todo.append(
            {"title": i.title, "completed": i.completed, "created_at": i.created_at}
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
