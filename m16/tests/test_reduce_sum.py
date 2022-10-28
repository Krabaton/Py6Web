import unittest
from unittest.mock import mock_open, patch, call
from src.reduce_sum.answer import numbers, sum_numbers
import src.reduce_sum.answer


class TestReduce(unittest.TestCase):
    """Test reduce method"""

    def test_result(self):
        """test result function"""
        result = sum_numbers(numbers)
        self.assertEqual(result, 96)

    @patch("src.reduce_sum.answer.other")
    def test_result_mock_other(self, mock_other):
        """test result function without other"""
        result = sum_numbers(numbers)
        self.assertEqual(result, 96)
        mock_other.assert_called()

    @patch("src.reduce_sum.answer.other")
    def test_result_mock_other_and_reduce(self, mock_other):
        """test result function without other, mock reduce"""
        with patch.object(src.reduce_sum.answer, 'reduce') as reduce_mock:
            reduce_mock.return_value = 96
            result = sum_numbers(numbers)
            self.assertEqual(result, 96)
            mock_other.assert_called()
            reduce_mock.assert_called()
