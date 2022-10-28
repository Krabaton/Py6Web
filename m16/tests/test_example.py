import unittest
from src.example.ops import add, sub, div, mul, async_add


class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set UP Class"""
        print('Start before all test')

    @classmethod
    def tearDownClass(cls):
        """Set Down Class"""
        print('Start after all test')

    def setUp(self):
        """Set UP for each test"""
        # print(f'Start before test: {self.shortDescription()}')

    def tearDown(self):
        """Set Down for each test"""
        # print(f'Start after test: {self.shortDescription()}')

    def test_add(self):
        """Add function test"""
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        """Sub function test"""
        self.assertEqual(sub(2, 3), -1)

    @unittest.skip("Функціонал ще не готовий")
    def test_div(self):
        """Div function test"""
        self.assertAlmostEqual(div(2, 3), 0.66666666)
        with self.assertRaises(ZeroDivisionError) as cm:
            div(1, 0)

    def test_mul(self):
        """Mul function test"""
        self.assertEqual(mul(2, 3), 6)


class TestAsyncExample(unittest.IsolatedAsyncioTestCase):

    async def test_async_add(self):
        result = await async_add(2, 3)
        self.assertEqual(5, result)
