from abc import ABC, abstractmethod


class BasicSort(ABC):

    @staticmethod
    def sort(array, with_trace=False):
        pass

    def trace(self):
        pass
