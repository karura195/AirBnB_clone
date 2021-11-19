#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.place import Place


class BaseModelTest(unittest.TestCase):
    """Test of the Place class"""
    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
