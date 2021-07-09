import unittest
import api


class TestApi(unittest.TestCase):
    def test_create_folder(self):
        result = api.create_folder('file')
        self.assertTrue(result == 201 or 409)

    def test_folder_existence(self):
        self.assertTrue(api.folder_existence('file') == 'dir')
