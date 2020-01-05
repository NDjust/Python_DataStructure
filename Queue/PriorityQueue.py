from LinkedList.DoublyLinkedList import DoublyLinkedList, Node


class PriorityQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.get_length()

    def is_empty(self):
        return self.data.get_length() == 0

    def enqueue(self, item):
        newNode = Node(item)
        curr = self.data.head

        # item < curr.next.data 을 먼저 비교하면 에러.
        while curr.next != self.data.tail and item < curr.next.data:
            curr = curr.next

        self.data.insert_after(curr, newNode)

    def dequeue(self):
        return self.data.pop_at(self.data.get_length())

    def peek(self):
        return self.data.get_at(self.data.get_length()).data
