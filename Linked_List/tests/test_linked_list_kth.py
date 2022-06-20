from Linked_List.linked_list_kth.linked_list_kth import Node, LinkedList

list = LinkedList()
list.insert(1)
list.append(2)
list.append(3)
list.append(4)


# def test_kth_one():
#
#   assert list.kth_from_end(2) == 3


# k grater that list length
def test_kth_one():

  assert list.kth_from_end(4) == 'invalid K'

# k and the length of the list are the same
def test_kth_two():

  assert list.kth_from_end(4) == 'invalid K'

#  k is not a positive integer
def test_kth_three():

  assert list.kth_from_end(-4) == 'invalid K'


#  linked list is of a size 1
def test_kth_four():
  list = LinkedList()
  list.insert(1)

  assert list.kth_from_end(0) == 1

# where k is not at the end, but somewhere in the middle of the linked list
def test_kth_five():

  assert list.kth_from_end(2) == 2