class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None


    def insert(self, value):

               if value is None:
                  raise Exception('Please insert value as argument')
               else:

                if value is None:
                    raise Exception('Please insert value as argument')
                else:

                    node = Node(value)
                    node.next = self.head
                    self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def to_string(self):

        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str += f" {current.value}  ->"
            current = current.next
        list_str += ' NULL'
        return list_str

    def append(self, value):

        node = Node(value)
        current = self.head
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert_after(self, value, new_value):

        current = self.head

        while current:

            if current.value == value:
                new_value = Node(new_value)
                new_value.next = current.next
                current.next = new_value
               # self._len += 1
                return True

            current = current.next

        return False

    def insert_before(self, value, new_Value):

        new_node = Node(new_Value)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            if self.head.value == value:
                node = self.head
                self.head = new_node
                new_node.next = node
                return True
            else:
                current = self.head
            while current.next != None:
                if current.next.value == value:
                    node = current.next
                    current.next = new_node
                    new_node.next = node
                    return True
                else:
                    current = current.next

            return False

    def kth_from_end(self, k):

        try:
            counter = -1
            current = self.head
            while current:
                current = current.next
                counter = counter + 1
            if counter >= k:
                current = self.head
                for i in range(counter - k):
                    current = current.next
                return current.value
            else:
                return 'invalid K'

        except:
            return "invalid K"

if __name__ == '__main__':
    list = LinkedList()
    list.insert(5)
    list.insert(9)
    list.insert_after(5,4)
    list.insert_before(5, 3)
    list.kth_from_end(1)



    print(list.to_string())
    print(list.kth_from_end(0))