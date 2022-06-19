from Linked_List.linked_list.Linked_list import LinkedList

def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None



def test_insert_to_empty():
    val = 6
    linked_list = LinkedList()
    linked_list.insert(val)
    assert linked_list.head.value == 6

def test_head_first_node():
   linked_list = LinkedList()
   linked_list.insert('1')
   assert linked_list.head.value == '1'
   linked_list.insert('2')
   assert linked_list.head.value == '2'
   linked_list.insert('3')
   assert linked_list.head.value == '3'
   linked_list.insert('4')
   assert linked_list.head.value == '4'
   linked_list.insert('5')
   assert linked_list.head.value == '5'

   assert linked_list.head.next.next.value == '3'



def test_insert_multiple():
    list = LinkedList()
    list.insert(1)
    list.insert("m")
    list.insert(3)
    list.insert("c")
    assert list.head.value == "c"
    assert list.head.next.value == 3
    assert list.head.next.next.value == "m"

# creating a Linked list to run the next tests
linked_list = LinkedList()
nodes = ['a', 'b', 1, 'm']
for node in nodes:
    linked_list.insert(node)

def test_includes_true():
    assert linked_list.includes('m') == True
    assert linked_list.includes(1) == True

def test_includes_false():
    assert linked_list.includes('k') == False
    assert linked_list.includes(4) == False

def test_string_str():
    assert linked_list.to_string() == ' m  -> 1  -> b  -> a  -> NULL'


