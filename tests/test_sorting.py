import unittest
from tip.algorithms.sorting.mergesort import mergesort


class TestMergesort(unittest.TestCase):

    def test_mergesort_basic(self):
        unsorted_list = [5, 3, 7, 8, 9, 3]
        sorted_list = mergesort(unsorted_list)
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_mergesort_trivial(self):
        unsorted_list = [1]
        sorted_list = mergesort(unsorted_list)
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_mergesort_with_duplicates(self):
        unsorted_list = [1, 1, 1, 1]
        sorted_list = mergesort(unsorted_list)
        self.assertEqual(sorted_list, sorted(unsorted_list))

    def test_mergesort_with_empty_list(self):
        unsorted_list = []
        sorted_list = mergesort(unsorted_list)
        self.assertEqual(sorted_list, sorted(unsorted_list))
