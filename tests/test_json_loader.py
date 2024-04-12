import json
import unittest
from datetime import datetime
from unittest.mock import mock_open, patch

from tododone.domain.todo import Todo
from tododone.domain.todo_list import TodoList
from tododone.utils.json_loader import JsonLoader


class TestJsonLoader(unittest.TestCase):
    def setUp(self):
        self.sample_json_data = json.dumps([
            {"id": 1, "description": "Test todo", "creation_date": "2023-01-01T00:00:00", "is_done": False}
        ])
        self.mock_file_path = "fake_path.json"

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("json.load")
    def test_load(self, mock_json_load, mock_open_file):
        mock_json_load.return_value = [
            Todo(1, "Test todo", datetime(2023, 1, 1, 0, 0), False)
        ]

        loader = JsonLoader()
        todo_list = loader.load(self.mock_file_path)

        mock_open_file.assert_called_once_with(self.mock_file_path, 'r')
        mock_json_load.assert_called_once()

        self.assertIsInstance(todo_list, TodoList)
        self.assertEqual(len(todo_list.todos), 1)
        self.assertEqual(todo_list.todos[0].description, "Test todo")

if __name__ == '__main__':
    unittest.main()
