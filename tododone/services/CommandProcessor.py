from tododone.domain import TodoList
from tododone.interfaces import IFileReader, IFileWriter

filename = "data/todos.json"
class CommandProcessor:
    def __init__(self, reader: IFileReader, writer: IFileWriter):
        self.reader: IFileReader = reader
        self.writer: IFileWriter = writer

        self.todo_list: TodoList = self.reader.load(filename)

    def process(self, action, option=""):
        if action == "add":
          description = option
          self.add(description)
        elif action == "remove":
          postIt_description = option
          self.remove(postIt_description)
        elif action == "mark_as_done":
            todo_id = option
            self.mark_as_done(todo_id)
        elif action == "show":
          self.show()
        # elif action == "export":
        #   self.export()
        else:
            print(f"Unknown action: {action}")

    def add(self, description: str):
        self.todo_list.add_todo(description)
        self.writer.save(self.todo_list, filename)

    def remove(self, todo_id: str):
        self.todo_list.remove_todo(todo_id)

    def show(self):
        print(self.todo_list)

    def mark_as_done(self, todo_id: str):
        self.todo_list.mark_todo_as_done(todo_id)

    # def export(self):
    #     self.writer.save(self.todo_lists, "postits.txt")
    #     print("postits exported!")