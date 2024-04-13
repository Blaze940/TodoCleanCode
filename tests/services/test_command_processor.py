import unittest
from unittest.mock import MagicMock, patch

from tododone.services.command_processor import CommandProcessor, filename


class TestCommandProcessor(unittest.TestCase):
    def setUp(self):
        # Mock dependencies
        self.reader = MagicMock()
        self.writer = MagicMock()
        self.exporter = MagicMock()

        # Create a TodoList instance for usage
        self.todo_list = MagicMock()

        # Configure the reader mock to return the TodoList
        self.reader.load.return_value = self.todo_list

        # Instantiate CommandProcessor with mocked dependencies
        self.processor = CommandProcessor(self.reader, self.writer, self.exporter)

    def test_init_loads_todos(self):
        """Test that the todo list is loaded during initialization."""
        self.reader.load.assert_called_once_with(filename)

    def test_process_add(self):
        """Test processing of 'add' action."""
        self.processor.process("add", "New task")
        self.todo_list.add_todo.assert_called_once_with("New task")
        self.writer.save.assert_called_once_with(self.todo_list, filename)

    def test_process_remove(self):
        self.processor.process("remove", "1")
        self.todo_list.remove_todo.assert_called_once_with("1")
        self.writer.save.assert_called_once_with(self.todo_list, filename)

    def test_process_mark_as_done(self):
        self.processor.process("mark_as_done", "1")
        self.todo_list.mark_todo_as_done.assert_called_once_with("1")
        self.writer.save.assert_called_once_with(self.todo_list, filename)

    def test_process_export(self):
        self.processor.process("export")
        self.exporter.export_done_todos.assert_called_once_with(self.todo_list)

    def test_process_unknown_action(self):
        with patch('builtins.print') as mocked_print:
            self.processor.process("unknown")
            mocked_print.assert_called_with("Unknown action: unknown")
            self.writer.save.assert_called_once_with(self.todo_list, filename)


if __name__ == '__main__':
    unittest.main()
