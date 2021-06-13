import unittest

from impl.bubble_sort import BubbleSort


class TestSort(unittest.TestCase):

    def test_bubble_sort_with_reverse_array(self):
        test_array = [i for i in range(5, 0, -1)]
        predict_array = [i for i in range(1, 6)]
        test_array = BubbleSort.sort(test_array)
        self.assertEqual(predict_array, test_array)

    def test_bubble_sort_with_mixed_array(self):
        test_array = [2, 4, 1, 0, 10, 1]
        predict_array = [0, 1, 1, 2, 4, 10]
        test_array = BubbleSort.sort(test_array)
        self.assertEqual(predict_array, test_array)


if __name__ == '__main__':
    unittest.main()
