class Node:

    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None
        self.nodeCount = 0

    def __repr__(self):
        if self.get_length() == 0:
            return "DoublyLinkedList is Empty!"

        s = ""

        current = self.head

        while current.next.next:
            current = current.next
            s += repr(current.data)

            if current.next.next is not None:
                s += " -> "

        return s

    def get_length(self):
        return self.nodeCount

    def get_at(self, pos):

        if pos < 0 or pos > self.nodeCount + 1:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head

            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def insert_after(self, prev, newNode):
        next = prev.next
        newNode.next = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1

        return True

    def insert_at(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.get_at(pos - 1)
        return self.insert_after(prev, newNode)

    def pop_after(self, prev):
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.nodeCount -= 1

        return curr.data

    def pop_at(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.get_at(pos - 1)
        return self.pop_after(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount

    def traversal(self):
        data_list = []

        current = self.head

        while current is not None:
            data_list.append(current.data)
            current = current.next

        return data_list


if __name__ == "__main__":
    node1 = Node(11)
    node2 = Node(22)
    node3 = Node(33)
    node4 = Node(44)
    node5 = Node(55)

    DL = DoublyLinkedList()

    DL.insert_at(1, node1)
    DL.insert_at(2, node2)
    DL.insert_at(1, node3)
    DL.insert_at(4, node4)

    print(DL)
    print(DL.traversal())

    DL.pop_at(1)
    DL.pop_at(2)
    DL.pop_at(2)

    print(DL)
