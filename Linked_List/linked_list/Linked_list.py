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






if __name__ == '__main__':
    list = LinkedList()
    list.insert(5)
    list.insert(9)
    list.insert(5)



    print(list.to_string())