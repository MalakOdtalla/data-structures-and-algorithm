import pytest
from Insertion_Sort import insertion_sort


def test_insertion_sort():
    array = [8, 4, 23, 42, 16, 15]
    Actual=array
    Expected=insertion_sort(array)
    # new_arr =[4, 8, 15, 16, 23, 42]


    assert Expected == Actual