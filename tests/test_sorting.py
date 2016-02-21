from tip.algorithms.sorting.mergesort import mergesort
from tip.algorithms.sorting.quicksort import quicksort
from tip.algorithms.sorting.insertion import insertionsort


class TestMergesort(object):
    """Test class for Merge Sort algorithm."""

    def test_mergesort_basic(self):
        """Test basic sorting."""
        unsorted_list = [5, 3, 7, 8, 9, 3]
        sorted_list = mergesort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_mergesort_trivial(self):
        """Test sorting when it's only one item."""
        unsorted_list = [1]
        sorted_list = mergesort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_mergesort_with_duplicates(self):
        """Test sorting a list with duplicates."""
        unsorted_list = [1, 1, 1, 1]
        sorted_list = mergesort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_mergesort_with_empty_list(self):
        """Test sorting a empty list."""
        unsorted_list = []
        sorted_list = mergesort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)


class TestQuicksort(object):
    """Test class for Quick Sort algorithm."""

    def test_quicksort_basic(self):
        """Test basic sorting."""
        unsorted_list = [5, 3, 7, 8, 9, 3]
        sorted_list = quicksort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_quicksort_trivial(self):
        """Test sorting when it's only one item."""
        unsorted_list = [1]
        sorted_list = quicksort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_quicksort_with_duplicates(self):
        """Test sorting a list with duplicates."""
        unsorted_list = [1, 1, 1, 1]
        sorted_list = quicksort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_quicksort_with_empty_list(self):
        """Test sorting a empty list."""
        unsorted_list = []
        sorted_list = quicksort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)


class TestInsertionsort(object):
    """Test class for Insertion Sort algorithm."""

    def test_insertionsort_basic(self):
        """Test basic sorting."""
        unsorted_list = [5, 3, 7, 8, 9, 3]
        sorted_list = insertionsort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_insertionsort_trivial(self):
        """Test sorting when it's only one item."""
        unsorted_list = [1]
        sorted_list = insertionsort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_insertionsort_with_duplicates(self):
        """Test sorting a list with duplicates."""
        unsorted_list = [1, 1, 1, 1]
        sorted_list = insertionsort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)

    def test_insertionsort_with_empty_list(self):
        """Test sorting a empty list."""
        unsorted_list = []
        sorted_list = insertionsort(unsorted_list)
        assert sorted_list == sorted(unsorted_list)
