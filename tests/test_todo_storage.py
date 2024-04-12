# import json
# import unittest
# from unittest.mock import mock_open, patch
#
# from tododone.services.todo_storage import TodoStorage
#
#
# class TestStorage(unittest.TestCase):
#     def setUp(self):
#         self.mock_open = mock_open(read_data="{'id': 1, 'content': 'test todo', 'done': False}")
#         self.patcher = patch('tododone.services.open', self.mock_open)
#         self.patcher.start()
#         self.storage = TodoStorage()
#
#     def tearDown(self):
#         self.patcher.stop()
#
#     def test_load_todos_empty_file(self):
#         self.assertEqual(self.storage.load_todos(), [])
#
#     def test_save_todos(self):
#         self.storage.postits = [{'id': 1, 'content': 'test todo', 'done': False}]
#         self.storage.save_todos()
#         expected_json = json.dumps(self.storage.postits, indent=4)
#         self.mock_open().write.assert_called_once_with(expected_json)
#
#     def test_add_todo(self):
#         todo = {'id': 2, 'content': 'another todo', 'done': True}
#         self.storage.add_todo(todo)
#         self.assertEqual(self.storage.postits, [todo])
#         self.mock_open().write.assert_called()
#
#     def test_delete_todo(self):
#         self.storage.postits = [{'id': 1, 'content': 'test todo', 'done': False}]
#         self.storage.delete_todo(1)
#         self.assertEqual(self.storage.postits, [])
#         self.mock_open().write.assert_called()
#
# if __name__ == '__main__':
#     unittest.main()