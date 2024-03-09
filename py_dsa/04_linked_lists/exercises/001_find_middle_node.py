class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = self.head
        slow = self.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

# Testing Arenas
assert my_linked_list.find_middle_node().value == 3


"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""