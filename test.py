import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    def test_get_doc_owner_name(self):
        print('test_get_doc_owner_name')
        doc_exist = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        with patch('builtins.input', return_value=doc_exist['number']):
            self.assertTrue(main.get_doc_owner_name() == doc_exist['name'])

    def test_add_new_doc(self):
        print('test_add_new_doc')
        new_doc = {"type": "passport", "number": "2208 886235", "name": "Василий Пупкин"}
        shelf = '1'
        with patch('builtins.input', side_effect=[new_doc['number'], new_doc['type'], new_doc['name'], shelf]):
            main.add_new_doc()
            self.assertIn(new_doc, main.documents)
            self.assertIn(new_doc["number"], main.directories[shelf])

    def test_delete_doc(self):
        print('test_delete_doc')
        doc_exist = {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        with patch('builtins.input', return_value=doc_exist["number"]):
            main.delete_doc()
            self.assertNotIn(doc_exist, main.documents)
            self.assertNotIn(doc_exist["number"], main.directories)
