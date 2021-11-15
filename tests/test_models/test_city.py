#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City


class BaseModelTest(unittest.TestCase):
    """Test of the City class"""
    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
