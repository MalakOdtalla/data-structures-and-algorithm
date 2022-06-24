from Linked_List.linked_list_insertions.linked_list_insertions import LinkedList

def zip_lists(list1, list2):
    counter_list1 = 0
    counter_list2 = 0

    current = list1.head
    while current != None:
        current = current.next
        counter_list1 += 1

    current = list2.head
    while current != None:
        current = current.next
        counter_list2 += 1

    if counter_list1 > counter_list2:
        l1 = list1
        l2 = list2
    else:
        l1 = list2
        l2 = list1

    current = l1.head
    current_list2 = l2.head
    while current != None and current_list2 != None:
        l1_next = current.next
        l2_next = current_list2.next
        current_list2.next = l1_next
        current.next = current_list2
        current = l1_next
        current_list2 = l2_next
    l2.head = current_list2
    return l1



if __name__ == '__main__':
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)


    list2 = LinkedList()
    list2.insert(3)
    list2.insert(4)
    list2.insert(3)




    print(list1.to_string())
    print(list2.to_string())



    print(zip_lists(list1,list2).to_string())