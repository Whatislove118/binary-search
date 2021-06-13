from abc import abstractmethod, ABC


class BasicSearch(ABC):

    @staticmethod
    def search(arr, sought_for_element, with_trace=False):
        pass

    @staticmethod
    def trace(arr):
        top_string = '------------------------ TRACE ------------------------'
        print(top_string)
        for i, element in enumerate(arr):
            pass

