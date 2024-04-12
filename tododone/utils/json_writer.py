import json

from tododone.domain import TodoList
from tododone.interfaces.IFileWriter import IFileWriter


class JsonWriter(IFileWriter):
    def save(self, todo_list: TodoList, path: str):
        data = todo_list.to_dict()
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
