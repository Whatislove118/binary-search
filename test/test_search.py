import unittest

from exceptions.ElementNotFoundException import ElementNotFoundException
from impl.binary_search import BinarySearch

class TestSearch(unittest.TestCase):

    def test_binary_search_with_sorted_array(self):
        arr = [i for i in range(6)]
        search_element = 6
        try:
            result_index = BinarySearch.search(arr, search_element)
            self.assertEqual(search_element, arr[result_index])
        except ElementNotFoundException as e:
            self.fail(e.err_msg)