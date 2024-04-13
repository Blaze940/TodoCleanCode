import unittest
from unittest.mock import MagicMock, mock_open, patch
from datetime import datetime
from tododone.domain.todo import Todo
from tododone.domain.todo_list import TodoList
from tododone.services.export_done_todos import DoneTodosExporter


class TestDoneTodosExporter(unittest.TestCase):
    def setUp(self):
        self.exporter = DoneTodosExporter()
        self.todos = [
            Todo(id=1, description="Completed task", creation_date=datetime(2023, 1, 1), is_done=True),
            Todo(id=2, description="Uncompleted task", creation_date=datetime(2023, 1, 2), is_done=False),
            Todo(id=3, description="Another completed task", creation_date=datetime(2023, 1, 3), is_done=True)
        ]
        self.todo_list = TodoList(self.todos)

    @patch('builtins.open', new_callable=mock_open)
    @patch('tododone.utils.todo_list_util.sort_todos')
    @patch('tododone.utils.todo_list_util.filter_done_todos')
    def test_export_done_todos(self, mock_filter_done_todos, mock_sort_todos, mock_file):
        # Setup the todo list with done todos
        mock_filter_done_todos.return_value = [todo for todo in self.todos if todo.is_done]
        mock_sort_todos.return_value = sorted(mock_filter_done_todos.return_value, key=lambda x: x.creation_date,
                                              reverse=True)

        expected_content = "# Report\n## Tasks done:\n\n"
        expected_content += "- Another completed task (2023-01-03)\n- Completed task (2023-01-01)"

        self.exporter.export_done_todos(self.todo_list, 'test_report.md')

        mock_file.assert_called_once_with('test_report.md', 'w')
        handle = mock_file()
        handle.write.assert_called_once_with(expected_content)


if __name__ == '__main__':
    unittest.main()
