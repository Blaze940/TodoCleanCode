import json
from pathlib import Path

class TodoStorage:
    def __init__(self, filename='todos.json'):
        self.path = Path(filename)
        self.todos = self.load_todos()

    def load_todos(self):
        """Load todos from a JSON file."""
        if self.path.exists():
            with self.path.open('r') as file:
                return json.load(file)
        return []

    def save_todos(self):
        """Save todos to a JSON file."""
        with self.path.open('w') as file:
            json.dump(self.todos, file, indent=4)

    def get_todos(self):
        """Return the list of todos."""
        return self.todos

    def add_todo(self, todo):
        """Add a new todo to the list and save to the file."""
        self.todos.append(todo)
        self.save_todos()

    def delete_todo(self, todo_id):
        """Delete a todo by id and save changes."""
        self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
        self.save_todos()

