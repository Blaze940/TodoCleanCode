from tododone.domain.todo_list import TodoList
from tododone.interfaces import IFileReader, IFileWriter
from tododone.services.export_done_todos import DoneTodosExporter

filename = "data/todos.json"


class CommandProcessor:
    def __init__(self, reader: IFileReader, writer: IFileWriter, doneTodosExporter: DoneTodosExporter):
        self.reader: IFileReader = reader
        self.writer: IFileWriter = writer
        self.doneTodosExporter: DoneTodosExporter = doneTodosExporter

        self.todo_list: TodoList = self.reader.load(filename)

    def process(self, action, option=""):
        if action == "add":
            description = option
            self.add(description)
        elif action == "remove":
            todo_description = option
            self.remove(todo_description)
        elif action == "mark_as_done":
            todo_id = option
            self.mark_as_done(todo_id)
        elif action == "show":
            self.show()
        elif action == "export":
            self.export()
        else:
            print(f"Unknown action: {action}")

        self.writer.save(self.todo_list, filename)

    def add(self, description: str):
        self.todo_list.add_todo(description)

    def remove(self, todo_id: str):
        self.todo_list.remove_todo(todo_id)

    def show(self):
        print(self.todo_list)

    def mark_as_done(self, todo_desc: str):
        self.todo_list.mark_todo_as_done(todo_desc)

    def export(self):
        self.doneTodosExporter.export_done_todos(self.todo_list)
