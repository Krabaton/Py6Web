import unittest
from unittest.mock import mock_open, patch, call
from src.save_data.answer import save_applicant_data, applicant


class TestSaveData(unittest.TestCase):
    mock_open_file = mock_open()

    @patch("builtins.open", mock_open_file)
    def test_open(self):
        """Test open file"""
        save_applicant_data(applicant, 'fake.csv')
        assert self.mock_open_file.call_count == 1, 'Open file only one'
        assert 'w' in self.mock_open_file.call_args[0], 'Open file only write mode'
        self.mock_open_file.assert_called_with('fake.csv', 'w')

    @patch("builtins.open", mock_open_file)
    def test_write(self):
        """Test write data"""
        save_applicant_data(applicant, 'fake.csv')
        calls = [
            call("Kovalchuk Oleksiy,301,175,180,155\n"),
            call("Karpenko Dmitro,201,155,175,185\n"),
            call("Ivanchuk Boryslav,101,135,150,165\n"),
        ]
        print(self.mock_open_file().write._mock_call_args_list)
        self.mock_open_file().write.assert_has_calls(calls, any_order=True)
