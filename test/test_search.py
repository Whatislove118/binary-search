import unittest

from exceptions.ElementNotFoundException import ElementNotFoundException
from impl.binary_search import BinarySearch
from impl.bubble_sort import BubbleSort


class TestSearch(unittest.TestCase):

    def test_binary_search_with_sorted_array(self):
        arr = [i for i in range(6)]
        search_element = 2
        try:
            result_index = BinarySearch.search(arr, search_element, with_trace=True)
            self.assertEqual(search_element, arr[result_index])
        except ElementNotFoundException as e:
            self.fail(e.err_msg)

    def test_binary_search_with_mixed_array(self):
        arr = [2, 4, 5, 6, 11, 2]
        search_element = 11
        try:
            result_index = BinarySearch.search(BubbleSort.sort(arr), search_element, with_trace=True)
            self.assertEqual(search_element, arr[result_index])
        except ElementNotFoundException as e:
            self.fail(e.err_msg)