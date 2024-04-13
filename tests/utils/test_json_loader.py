import unittest
from unittest.mock import patch, mock_open

from tododone.utils.json_loader import JsonLoader


class TestJsonLoader(unittest.TestCase):
    def setUp(self):
        self.sample_json_data = '[{"id": 1, "content": "Finish the report", "done": False}]'
        self.loader = JsonLoader()

    @patch("builtins.open", new_callable=mock_open,
           read_data='[{"id": 1, "content": "Finish the report", "done": False}]')
    @patch("json.load")
    def test_load_todos(self, mock_json_load, mock_file):
        # Given
        mock_json_load.return_value = [{"id": 1, "content": "Finish the report", "done": False}]

        # When
        result = self.loader.load("dummy_path.json")

        # Then
        mock_file.assert_called_once_with("dummy_path.json", 'r')
        mock_json_load.assert_called_once()  # Ensures json.load was called once
        self.assertEqual(result, [{"id": 1, "content": "Finish the report", "done": False}])
        self.assertIsInstance(result, list)  # Ensure that result is a list


if __name__ == '__main__':
    unittest.main()
