import datetime
import unittest

from tododone.domain.Postit import PostIt
from tododone.domain.Todo import Todo


class MyTestCase(unittest.TestCase):

    def test_should_list_all_todos(self):
        # Given
        postits: list[PostIt] = [
            PostIt(1, "toto", datetime.date.today()),
            PostIt(2, "tata", datetime.date.today())
        ]
        todo = Todo(postits)
        # When
        result = todo.get_all_todos()

        # Then
        self.assertEqual(postits, result)

    def test_should_add_postit(self):
        # Given
        todo = Todo([])
        postit = PostIt(1, "toto", datetime.date.today())

        # When
        todo.add(postit)

        # Then
        self.assertIn(postit, todo.todos)

    def test_should_remove_postit(self):
        # Given
        postit = PostIt(1, "toto", datetime.date.today())
        todo = Todo([postit])

        # When
        todo.remove(postit)

        # Then
        self.assertNotIn(postit, todo.todos)

    def test_should_mark_as_done(self):
        # Given
        postit = PostIt(1, "toto", datetime.date.today())
        todo = Todo([postit])
        # When
        todo.mark_as_done(postit.id)

        # Then
        self.assertEqual(postit.is_done, True)


if __name__ == '__main__':
    unittest.main()
