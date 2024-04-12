from tododone.domain.todo_list import TodoList


class IFileWriter:
    def save(self, todo_list: TodoList, path: str):
        pass