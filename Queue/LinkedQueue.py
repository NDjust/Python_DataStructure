from LinkedList.DoublyLinkedList import DoublyLinkedList, Node

# Test Case 해볼 것.
class LinkedQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.get_length()

    def is_empty(self):
        return self.data.get_length() == 0

    def enqueue(self, item):
        newNode = Node(item)

        self.data.insert_after(self.tail, newNode)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")

        return self.data.pop_at(self.data.get_length())

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")

        return self.data.get_at(self.data.get_length()).datas