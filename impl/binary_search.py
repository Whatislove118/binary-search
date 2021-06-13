from basic_classes.basic_search import BasicSearch
import math

from exceptions.ElementNotFoundException import ElementNotFoundException


class BinarySearch(BasicSearch):

    @staticmethod
    def search(arr, sought_for_element, with_trace=False):
        left_bound, right_bound = 0, len(arr)
        for i in arr:
            mid = math.floor((right_bound + left_bound) / 2)  # round down
            if sought_for_element == arr[mid]:
                return mid
            elif sought_for_element < arr[mid]:
                right_bound = mid
            elif sought_for_element > arr[mid]:
                left_bound = mid
        raise ElementNotFoundException()

            


    @staticmethod
    def trace(arr):
        pass