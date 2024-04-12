import datetime

from tododone.domain.Todo import Todo


class TodoList:
    def __init__(self, todos: list[Todo]):
        self.todos: list[Todo] = todos

    def add_todo(self, todo_description: str):
        todo = Todo(id=len(self.todos) + 1, description=todo_description, creation_date=datetime.datetime.now())
        self.todos.append(todo)
        print("New Todo added!")

    def remove_todo(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                self.todos.remove(todo)
        print(f"todo_id [{todo_id}] removed!")

    def get_all_todos(self):
        return self.todos

    def get_one_todo(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo

    def mark_todo_as_done(self, todo_id: str):
        todo = self.get_one_todo(todo_id)
        todo.is_done = True
        print(f"Todo [{todo.description}] marked as done!")
        return todo

    def to_dict(self):
        return [todo.to_dict() for todo in self.todos]

    def __str__(self):
        display = ""
        for todo in self.todos:
            display += f"{todo}\n"
        return display
