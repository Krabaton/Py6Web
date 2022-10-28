import unittest
from unittest.mock import mock_open, patch
from src.method.main import read_contacts_from_file, write_contacts_to_file, ttt


class TestSaveData(unittest.TestCase):
    contacts = [{"firstname": "Natalia", "age": 18}, {"firstname": "Vova", "age": 90}]
    mock_open_file = mock_open()

    @patch("json.dump")
    def test_open(self, dump_mock):
        ttt()
        dump_mock.assert_called()

    @patch("json.dump")
    @patch("builtins.open", mock_open_file)
    def test_write_contacts_to_file(self, dump_mock):
        write_contacts_to_file('test.json', self.contacts)
        self.mock_open_file.assert_called_with('test.json', 'w')
        dump_mock.assert_called()
        dump_mock.assert_called_with({"contacts": self.contacts}, self.mock_open_file())

    @patch("json.load")
    @patch("builtins.open", mock_open_file)
    def test_read_contacts_from_file(self, load_mock):
        load_mock.return_value = {"contacts": self.contacts}
        result = read_contacts_from_file('test.json')
        self.mock_open_file.assert_called_with('test.json', 'r')
        load_mock.assert_called()
        load_mock.assert_called_with(self.mock_open_file())
        self.assertListEqual(result, self.contacts)



