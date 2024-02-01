from node import Node


class LinkedList:
    """Class representing the ADT: Linked-List"""

    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        if value is not None:
            new_node = Node(value)
            self.head = self.tail = new_node
            self.length = 1

    def append(self, value):
        """ Insert a new Node at the end of the Linked List"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return self.head
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        return self.head

    def prepend(self, value):
        """ Insert a value at the beginning of the LinkedList"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return self.head
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.head

    def insert(self, value, index):
        """ Creates a new node, and inserts it at a desired index.
        If index is higher than the length, IndexError is raised."""

        if index >= self.length or index < 0:
            raise IndexError("Index provided is out of range.")
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        temp_ptr = self.head
        for i in range(0, self.length):
            if i + 1 == index:
                new_node.next = temp_ptr.next
                temp_ptr.next = new_node
                self.length += 1
                break
            temp_ptr = temp_ptr.next
        temp_ptr = None  # clear temp_ptr
        return self.head

    def print_list_nodes(self):
        """Prints all the node"""
        if not self.head:
            return
        my_ptr = self.head
        while my_ptr:
            print(my_ptr.value)
            my_ptr = my_ptr.next


# Tests Arena
myLL = LinkedList(12)
myLL.print_list_nodes()
myLL.append(13)
myLL.print_list_nodes()
myLL.prepend(10)
myLL.print_list_nodes()
myLL.insert(11, 1)
myLL.print_list_nodes()
