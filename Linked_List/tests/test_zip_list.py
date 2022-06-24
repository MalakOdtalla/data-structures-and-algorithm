from Linked_List.linked_list_insertions.linked_list_insertions import LinkedList
from Linked_List.linked_list_zip.linked_list_zip import zip_lists
import pytest

def test_zip_lists1():
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)

    list2 = LinkedList()
    list2.insert(3)
    list2.insert(4)

    assert zip_lists(list1, list2).to_string()==  " 4  -> 2  -> 3  -> 1  -> NULL"

def test_zip_lists2():
        list1 = LinkedList()
        list1.insert(1)
        list1.insert(2)
        list1.insert(5)

        list2 = LinkedList()
        list2.insert(3)
        list2.insert(4)

        assert zip_lists(list1, list2).to_string() == " 5  -> 4  -> 2  -> 3  -> 1  -> NULL"

def test_zip_lists3():
            list1 = LinkedList()
            list1.insert(1)
            list1.insert(2)

            list2 = LinkedList()
            list2.insert(3)
            list2.insert(4)
            list2.insert(5)

            assert zip_lists(list1, list2).to_string() == " 5  -> 2  -> 4  -> 1  -> 3  -> NULL"