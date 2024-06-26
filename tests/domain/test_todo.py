import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from tododone.domain.todo import Todo


class TestTodo(unittest.TestCase):
    def test_to_dict(self):
        creation_date = datetime(2020, 5, 20, 15, 30)
        todo = Todo(1, "Write unit tests", creation_date, is_done=True)
        expected_dict = {
            'id': 1,
            'description': "Write unit tests",
            'creation_date': "2020-05-20T15:30:00",
            'is_done': True
        }
        self.assertEqual(todo.to_dict(), expected_dict)

    def test_time_elapsed_years(self):
        creation_date = datetime.now() - timedelta(days=365 * 2 + 30)  # More than 2 years ago
        todo = Todo(1, "Project started", creation_date)
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = datetime.now()
            self.assertEqual(todo.time_elapsed(), "2 years")

    def test_time_elapsed_months(self):
        creation_date = datetime.now() - timedelta(days=30 * 3)  # 3 months ago
        todo = Todo(2, "Write documentation", creation_date)
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = datetime.now()
            self.assertEqual(todo.time_elapsed(), "3 months")

    def test_time_elapsed_days(self):
        creation_date = datetime.now() - timedelta(days=10)  # 10 days ago
        todo = Todo(3, "Update codebase", creation_date)
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = datetime.now()
            self.assertEqual(todo.time_elapsed(), "10 days")

    def test_time_elapsed_hours(self):
        creation_date = datetime.now() - timedelta(hours=5)  # 5 hours ago
        todo = Todo(4, "Refactor components", creation_date)
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = datetime.now()
            self.assertEqual(todo.time_elapsed(), "5 hours")

    def test_time_elapsed_minutes(self):

        creation_date = datetime.now() - timedelta(minutes=30)
        todo = Todo(5, "Fix bugs", creation_date)
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = datetime.now()
            self.assertEqual(todo.time_elapsed(), "30 min")

    def test_time_elapsed_just_now(self):
        creation_date = datetime.now()  # Momentarily
        todo = Todo(6, "Deploy app", creation_date)
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = datetime.now()
            self.assertEqual(todo.time_elapsed(), "Just now")


if __name__ == '__main__':
    unittest.main()
