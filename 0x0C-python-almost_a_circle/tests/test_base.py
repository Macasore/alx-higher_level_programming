import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_idnone(self):
        """test_id function
        Tests that the logic for id works as
        expected i.e initialises object with id if specified
        or defaults to number of instances with default ids
        """
        b1 = Base()
        b2 = Base(None)
        b3 = Base(12)
        b5 = Base(-5)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
