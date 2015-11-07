import unittest
from tip.algorithms.sorting.mergesort import mergesort


class TestSorting(unittest.TestCase):

    def test_mergesort(self):
        unsorted_list = [5, 3, 7, 8, 9, 3]
        sorted_list = mergesort(unsorted_list)
        self.assertEqual(sorted_list, sorted(unsorted_list))
