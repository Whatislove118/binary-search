# :clipboard: :mag: Binary-search
## Project №1 for CV
**This code realizes the `Binary Search` algorithm in `Python`.**
### Description
This code provides a `binary search` algorithm. `Bubble sort` is used to sort the array. It also provides the ability to output a trace.
### Code architecture
This program contains two basic classes:
* `BasicSearch` class with two static methods: `search` and `trace`
* `BasicSort` class with two static methods: `sort` and `trace`

*You always can implement this classes and create your own realization of another algorithms.*

And two classes with implemented algorithms:
* `BinarySearch`
* `BubbleSort`
### Method description
* `search` method requires two required arguments - an `array` and the `sought_for_element` to be searched for, and one optional - `with_trace`, which indicates whether to output a trace or not (`False` by default). This method returns the `index` in the array in which the searched element is located. If the element is not found, an exception `ElementNotFoundException` is thrown.
* `sort` method has one required argument - an `array` to be sorted and an optional argument `with_trace`. Returns the same array, only sorted.
* `trace` method has two required arguments - `array` and `changed_array`
### Code usages
For examples look for two test files in package `test` (`test_search.py` and `test_sort.py`)

 
