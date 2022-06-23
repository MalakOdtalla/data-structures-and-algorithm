from Linked_List.linked_list_insertions.linked_list_insertions import LinkedList

def zip_lists(list1, list2):
    new_list = LinkedList()
    current_list1 = list1.head
    current_list2 = list2.head
    if not list1 :
        return list1
    if not list2 :
        return list1

    while current_list1:
        new_list.append(current_list1.value)
        if current_list2 :
            new_list.append(current_list2.value)
            current_list2 = current_list2.next
        current_list1= current_list1.next
    while current_list2 :
        new_list.append(current_list2.value)
        current_list2 =current_list2.next
    return new_list

if __name__ == '__main__':
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)

    list2 = LinkedList()
    list2.insert(3)
    list2.insert(4)

    print(list1.to_string())
    print(list2.to_string())



    print(zip_lists(list1,list2).to_string())