import unittest
from datetime import datetime

from tododone.domain.todo import Todo
from tododone.domain.todo_list import TodoList
from tododone.utils.todo_list_util import filter_done_todos, sort_todos


class TestTodoUtilities(unittest.TestCase):
    def setUp(self):
        self.todos = [
            Todo(1,"Task 1", datetime(2024, 3, 10, 15, 30), False),
            Todo(2,"Task 2", datetime(2024, 3, 9, 16, 45), True),
            Todo(3,"Task 3", datetime(2024, 3, 8, 14, 0), True)
        ]
        self.todo_list = TodoList(self.todos)

    def test_filter_done_todos(self):
        done_todos = filter_done_todos(self.todo_list)
        self.assertEqual(len(done_todos), 2)
        for todo in done_todos:
            self.assertTrue(todo.is_done)

    def test_sort_todos_ascending(self):
        sorted_todos = sort_todos(self.todos, descending=False)
        self.assertEqual(sorted_todos, [self.todos[2], self.todos[1], self.todos[0]])

    def test_sort_todos_descending(self):
        sorted_todos = sort_todos(self.todos, descending=True)
        self.assertEqual(sorted_todos, [self.todos[0], self.todos[1], self.todos[2]])

if __name__ == '__main__':
    unittest.main()
