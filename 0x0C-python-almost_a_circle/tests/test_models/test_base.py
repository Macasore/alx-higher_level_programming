import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_idnone(self):
        b1 = Base()
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


