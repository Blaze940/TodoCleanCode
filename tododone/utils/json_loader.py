import json
from datetime import datetime

from tododone.domain.Todo import Todo
from tododone.domain.TodoList import TodoList
from tododone.interfaces.IFileReader import IFileReader


class JsonLoader(IFileReader):
    def load(self, path: str) -> TodoList:
        def decoder(dct):
            if 'id' in dct and 'description' in dct and 'creation_date' in dct and 'is_done' in dct:
                return Todo(dct['id'], dct['description'],
                            datetime.strptime(dct['creation_date'], '%Y-%m-%dT%H:%M:%S'), dct['is_done'])
            return dct

        with open(path, 'r') as file:
            todos_data = json.load(file, object_hook=decoder)
            return TodoList(todos=todos_data)

