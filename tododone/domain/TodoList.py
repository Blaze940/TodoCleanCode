import datetime

from tododone.domain.Todo import Todo


class TodoList:
    def __init__(self, todos: list[Todo]):
        self.todos: list[Todo] = todos

    def add_todo(self, todo_description: str):
        todo = Todo(id=len(self.todos) + 1, description=todo_description, creation_date=datetime.datetime.now())
        self.todos.append(todo)
        print("New Todo added!")

    def remove_todo(self, todo_desc):
        todo = self.get_one_todo(todo_desc)
        if todo:
            self.todos.remove(todo)
            print(f"Todo [{todo_desc}] removed!")
        else:
            print(f"Todo with description [{todo_desc}] not found.")

    def get_all_todos(self):
        return self.todos

    def get_one_todo(self, todo_desc):
        for todo in self.todos:
            print(todo.description, todo_desc)
            if todo.description == todo_desc:
                return todo
        return None

    def mark_todo_as_done(self, todo_desc):
        todo = self.get_one_todo(todo_desc)
        if todo:
            todo.is_done = True
            print(f"Todo [{todo.description}] marked as done!")
        else:
            print(f"Todo with id {todo_desc} not found.")

    def to_dict(self):
        return [todo.to_dict() for todo in self.todos]

    def __str__(self):
        return "\n".join(str(todo) for todo in self.todos)
