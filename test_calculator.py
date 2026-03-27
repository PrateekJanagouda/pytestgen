import unittest

class TestMathFunctions(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), -6)

    def test_multiply_mixed_number(self):
        self.assertEqual(multiply(2, -3), -6)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(4, 2), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-4, -2), 2)

    def test_divide_mixed_number(self):
        self.assertEqual(divide(-4, -2), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(4, 0)

if __name__ == '__main__':
    unittest.main()