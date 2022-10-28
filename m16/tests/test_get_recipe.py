import unittest
from unittest.mock import mock_open, patch
from src.get_recipe.get_recipe import get_recipe


class TestGetRecipe(unittest.TestCase):
    mock_open_file = None

    @classmethod
    def setUpClass(cls):
        cls.mock_open_file = mock_open(read_data='60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red '
                                                 'onion,2 tablespoons chopped fresh basil\n60b90c2413067a15887e1ae2,'
                                                 'Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored '
                                                 'almond milk,1 lemon')

    @classmethod
    def tearDownClass(cls):
        cls.mock_open_file = None

    def test_get_first_recipe(self):
        """Test first recipe"""
        uid = "60b90c1c13067a15887e1ae1"
        file = "fake.csv"
        with patch("builtins.open", self.mock_open_file) as mock_file:
            result = get_recipe(file, uid)
            self.assertEqual(uid, result.get("id"))
            self.assertEqual("Herbed Baked Salmon", result.get("name"))

    def test_get_second_recipe(self):
        """Test second recipe"""
        uid = "60b90c2413067a15887e1ae2"
        file = "fake.csv"
        with patch("builtins.open", self.mock_open_file) as mock_file:
            result = get_recipe(file, uid)
            self.assertEqual(uid, result.get("id"))
            self.assertEqual("Lemon Pancakes", result.get("name"))