from abc import ABC, abstractmethod


class BasicSort(ABC):

    @staticmethod
    def sort(array, with_trace=False):
        pass

    @staticmethod
    def trace(array, changed_array):
        print('{} -> {}'.format(array, changed_array))

