"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """Test adding 2 numbers"""
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """Test minus 2 numbers"""
        res = calc.subtract(2, 5)
        self.assertEqual(res, 3)