import unittest
from unittest.mock import MagicMock, patch, create_autospec

from tododone.domain.todo_list import TodoList
from tododone.interfaces import IFileReader, IFileWriter
from tododone.services.command_processor import CommandProcessor
from tododone.services.export_done_todos import DoneTodosExporter


class TestCommandProcessor(unittest.TestCase):
    def setUp(self):
        self.reader = create_autospec(IFileReader, instance=True)
        self.writer = create_autospec(IFileWriter, instance=True)
        self.exporter = create_autospec(DoneTodosExporter, instance=True)

        self.todo_list = MagicMock(spec=TodoList)
        self.reader.load.return_value = self.todo_list

        self.processor = CommandProcessor(self.reader, self.writer, self.exporter)

    def test_process_add(self):
        """ Test 'add' action processing """
        self.processor.process("add", "New task")
        self.todo_list.add_todo.assert_called_once_with("New task")
        self.writer.save.assert_called_once_with(self.todo_list, "data/todos.json")

    def test_process_remove(self):
        """ Test 'remove' action processing """
        self.processor.process("remove", "New task")
        self.todo_list.remove_todo.assert_called_once_with("New task")
        self.writer.save.assert_called_once_with(self.todo_list, "data/todos.json")

    def test_process_mark_as_done(self):
        """ Test 'mark_as_done' action processing """
        self.processor.process("mark_as_done", "New task")
        self.todo_list.mark_todo_as_done.assert_called_once_with("New task")
        self.writer.save.assert_called_once_with(self.todo_list, "data/todos.json")

    def test_process_show(self):
        """ Test 'show' action processing """
        with patch('builtins.print') as mocked_print:
            self.processor.process("show")
            mocked_print.assert_called_once()
            self.todo_list.__str__.assert_called_once()

    def test_process_export(self):
        """ Test 'export' action processing """
        self.processor.process("export")
        self.exporter.export_done_todos.assert_called_once_with(self.todo_list)

    def test_process_unknown(self):
        """ Test handling of an unknown action """
        with patch('builtins.print') as mocked_print:
            self.processor.process("unknown_action")
            mocked_print.assert_called_with("Unknown action: unknown_action")
            self.writer.save.assert_called_once_with(self.todo_list, "data/todos.json")


if __name__ == '__main__':
    unittest.main()
