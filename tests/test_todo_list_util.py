import unittest
from datetime import datetime

from tododone.domain.Todo import Todo
from tododone.domain.TodoList import TodoList
from tododone.utils.todo_list_util import filter_done_todos, sort_todos


class TestTodoUtilities(unittest.TestCase):
    def setUp(self):
        self.todos = [
            Todo("Task 1", datetime(2024, 3, 10, 15, 30), False),
            Todo("Task 2", datetime(2024, 3, 9, 16, 45), True),
            Todo("Task 3", datetime(2024, 3, 8, 14, 0), True)
        ]
        self.todo_list = TodoList(self.todos)

    def test_filter_done_todos(self):
        """Test only completed todos are returned."""
        done_todos = filter_done_todos(self.todo_list)
        self.assertEqual(len(done_todos), 2)  # Check that two todos are returned
        for todo in done_todos:
            self.assertTrue(todo.is_done)  # Each todo should be marked as done

    def test_sort_todos_ascending(self):
        """Test todos are sorted by creation date in ascending order."""
        sorted_todos = sort_todos(self.todos, ascending=True)
        self.assertEqual(sorted_todos, [self.todos[2], self.todos[1], self.todos[0]])

    def test_sort_todos_descending(self):
        """Test todos are sorted by creation date in descending order."""
        sorted_todos = sort_todos(self.todos, ascending=False)
        self.assertEqual(sorted_todos, [self.todos[0], self.todos[1], self.todos[2]])

if __name__ == '__main__':
    unittest.main()
