"""Doubly Linked List Module"""
from node import Node


class DoublyLinkedList:
    def __init__(self, value=None):
        """Doubly Linked List Constructor"""
        self.head = None
        self.tail = None
        self.length = 0
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def prepend(self, value=None):
        """Adds a new Node to the beginning of the Doubly-LinkedList."""
        if not self.head:
            return self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return self.head

    def append(self, value=None):
        """Appends a new Node to the end of the Doubly-LinkedList."""
        new_node = new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return new_node
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self.tail

    def pop(self):
        """Removes the Node at the end of a Linked-List. This could also be the last Node."""
        temp = None # temporary pointer
        if self.head == self.tail:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.tail
            self.tail = temp.prev
            temp.prev = None
            self.tail.next = None
            self.length -= 1
        return temp

    def pop_first(self):
        """Removes the first Node from the DLL. It may also be the very last Node if there is only 1 Node left.."""
        if not self.head:
            return None
        if self.head == self.tail:
            return self.pop()
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """Given an index value, returns the Node at that given index."""
        if not self.head or index >= self.length or index < 0:
            return None
        if index >= self.length // 2:
            i = self.length - 1
            temp = self.tail
            while temp:
                if i == index:
                    return temp
                i -= 1
                temp = temp.prev
        else:
            i = 0
            temp = self.head
            while temp:
                if i == index:
                    return temp
                i += 1
                temp = temp.next

    def set_value(self, index, value):
        """Given an index value, updates the value of the Node at that given index."""
        node = self.get(index)
        if node:
            node.value = value
        return node

    def insert(self, index, value):
        """Given an index value, inserts a new Node at that index."""
        if index < 0 or index > self.length:
            print("IndexError: Invalid index. Index of range bound.")
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prev_node = self.get(index - 1)
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node
        self.length += 1
        return self.head
