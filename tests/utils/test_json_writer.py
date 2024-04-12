import json
import unittest
from unittest.mock import patch, mock_open

from tododone.domain.todo_list import TodoList
from tododone.utils.json_writer import JsonWriter


class TestJsonWriter(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList([])
        self.todo_list.to_dict = lambda: [{'id': 1, 'description': 'Complete unit tests', 'is_done': False}]
        self.path = "fake_path.json"
        self.json_data = json.dumps(self.todo_list.to_dict(), indent=4)

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save(self, mock_json_dump, mock_open_file):
        writer = JsonWriter()
        writer.save(self.todo_list, self.path)

        mock_open_file.assert_called_once_with(self.path, 'w')

        mock_json_dump.assert_called_once_with(self.todo_list.to_dict(), mock_open_file(), indent=4)

if __name__ == '__main__':
    unittest.main()
