def todo_serializer(todo) -> dict:
    return{
        "id":str(todo['_id']),
        "name":str(todo["name"]),
        "description":str(todo["description"]),
         "completed": todo["completed"],
         "date": todo["date"],
    }


def todos_serializer(todos) -> list:
    return [todo_serializer(todo) for todo in todos] 