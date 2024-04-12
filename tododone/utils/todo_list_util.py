from tododone.domain import TodoList

def filter_done_todos(todo_list: TodoList):
    return [todo for todo in todo_list.todos if todo.is_done]


def sort_todos(todos: TodoList, ascending: bool = True):
    return sorted(todos, key=lambda x: x.creation_date, reverse=ascending)