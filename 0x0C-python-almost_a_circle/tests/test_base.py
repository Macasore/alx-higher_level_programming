import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_idnone(self):
        b1 = Base()
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_idvalue(self):
        b3 = Base(12)
        b5 = Base(-5)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b5.id, -5)
