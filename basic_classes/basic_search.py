from abc import abstractmethod, ABC


class BasicSearch(ABC):

    @staticmethod
    def search(arr, sought_for_element, with_trace=False):
        pass

    @staticmethod
    def trace(arr, changed_arr):
        print('{} -> {}'.format(arr, changed_arr))


