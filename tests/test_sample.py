import unittest
from tip.algorithms.dummy import dummy_add


class TestDummyAdd(unittest.TestCase):

    def test_lcm(self):
        r = dummy_add(2, 2)
        self.assertEqual(r, 4)
