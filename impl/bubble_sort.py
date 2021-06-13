from basic_classes.basic_sort import BasicSort


class BubbleSort(BasicSort):

    @staticmethod
    def sort(array, with_trace=False) -> list:
        is_swapped = True
        while is_swapped:
            is_swapped = False

            for i, element in enumerate(array):
                if i == len(array) - 1: continue
                if element > array[i + 1]:
                    array[i] = array[i + 1]
                    array[i + 1] = element
                    is_swapped = True

        return array
        # 5 4 3 2 1 -> 4 5 3 2 1


    def trace(self):
        pass
