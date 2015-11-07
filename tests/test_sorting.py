from tip.algorithms.sorting.mergesort import mergesort


class TestMergesort():
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
