import unittest
from unittest.mock import patch, MagicMock
from tododone.domain import TodoList
from tododone.services.export_done_todos import DoneTodosExporter


class TestDoneTodosExporter(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('tododone.utils.todo_list_util.filter_done_todos')
    @patch('tododone.utils.todo_list_util.sort_todos')
    def test_export_done_todos(self, mock_sort_todos, mock_filter_done_todos, mock_open):
        # Set up mocks for the filter and sort functions
        mock_todo1 = MagicMock(description="Completed Task 1", creation_date="2024-03-09")
        mock_todo2 = MagicMock(description="Completed Task 2", creation_date="2024-03-02")

        # Mocking behavior of filter and sort utilities
        mock_filter_done_todos.return_value = [mock_todo1, mock_todo2]
        mock_sort_todos.return_value = [mock_todo2, mock_todo1]  # Sorted by date

        # Mock TodoList
        todo_list = MagicMock(spec=TodoList)

        # Create instance of DoneTodosExporter
        exporter = DoneTodosExporter()

        # Execute the method under test
        exporter.export_done_todos(todo_list, 'dummy_report.md')

        # Check calls to filter and sort utilities
        mock_filter_done_todos.assert_called_once_with(todo_list)
        mock_sort_todos.assert_called_once_with([mock_todo1, mock_todo2], ascending=False)

        # Ensure file operations are performed correctly
        mock_open.assert_called_once_with('dummy_report.md', 'w')
        handle = mock_open()
        handle.write.assert_called_once_with(
            "# Report\n## Tasks done:\n\n" + "- Completed Task 2 (2024-03-02)\n- Completed Task 1 (2024-03-09)")
        print("Report generation test passed.")


if __name__ == '__main__':
    unittest.main()
