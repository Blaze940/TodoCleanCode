import datetime
import unittest

from tododone.domain.Todo import Todo
from tododone.domain.TodoList import TodoList


class TestToDo(unittest.TestCase):

    def test_should_list_all_todos(self):
        # Given
        postits: list[Todo] = [
            Todo(1, "toto", datetime.date.today()),
            Todo(2, "tata", datetime.date.today())
        ]
        todo = TodoList(postits)
        # When
        result = todo.get_all_todos()

        # Then
        self.assertEqual(postits, result)

    def test_should_add_postit(self):
        # Given
        todo = TodoList([])
        postit = Todo(1, "toto", datetime.date.today())

        # When
        todo.add_todo(postit)

        # Then
        self.assertIn(postit, todo.todos)

    def test_should_remove_postit(self):
        # Given
        postit = Todo(1, "toto", datetime.date.today())
        todo = TodoList([postit])

        # When
        todo.remove_todo(postit)

        # Then
        self.assertNotIn(postit, todo.todos)

    def test_should_mark_as_done(self):
        # Given
        postit = Todo(1, "toto", datetime.date.today())
        todo = TodoList([postit])
        # When
        todo.mark_todo_as_done(postit.id)

        # Then
        self.assertEqual(postit.is_done, True)


if __name__ == '__main__':
    unittest.main()
