"""
sample test
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests for the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test Subtracting numbers"""
        res = calc.subtract(5, 6)
        self.assertEqual(res, 1)
