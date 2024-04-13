import unittest
from unittest.mock import patch
from tododone.domain.todo import Todo
import datetime

from tododone.domain.todo_list import TodoList


class TestTodoList(unittest.TestCase):
    def setUp(self):
        """ Setup a known state of TodoList before each test """
        self.todos = [
            Todo(id=1, description="Write unit tests", creation_date=datetime.datetime.now()),
            Todo(id=2, description="Create presentation", creation_date=datetime.datetime.now())
        ]
        self.todo_list = TodoList(self.todos)

    def test_add_todo(self):
        """ Test the add_todo method """
        self.todo_list.add_todo("Finish report")
        self.assertEqual(len(self.todo_list.todos), 3)
        self.assertEqual(self.todo_list.todos[-1].description, "Finish report")

    def test_remove_todo(self):
        self.todo_list.remove_todo("Write unit tests")
        self.assertEqual(len(self.todo_list.todos), 1)
        self.assertNotIn(1, [todo.id for todo in self.todo_list.todos])

    def test_remove_todo_not_found(self):
        with patch('builtins.print') as mocked_print:
            self.todo_list.remove_todo("Oh")
            mocked_print.assert_called_with("Todo with description [Oh] not found.")

    def test_get_one_todo(self):
        todo = self.todo_list.get_one_todo("Write unit tests")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.description, "Write unit tests")

    def test_mark_todo_as_done(self):
        self.todo_list.mark_todo_as_done("Write unit tests")
        self.assertTrue(self.todo_list.todos[0].is_done)

    def test_mark_todo_as_done_not_found(self):
        with patch('builtins.print') as mocked_print:
            self.todo_list.mark_todo_as_done("99")
            mocked_print.assert_called_with("Todo with id [99] not found.")

if __name__ == '__main__':
    unittest.main()
