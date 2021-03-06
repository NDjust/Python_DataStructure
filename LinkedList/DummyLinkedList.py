class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class DummyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail
        self.nodeCount = 0

    def __repr__(self):
        if self.nodeCount == 0:
            return "Dummy LinkedList is Empty!"

        s = ""
        curr = self.head

        while curr.next:
            curr = curr.next
            s += repr(curr.data)

            if curr.next is not None:
                s += " -> "

        return s

    def get_length(self):
        return self.nodeCount

    def get_at(self, pos):
        if pos < 0 or pos > self.nodeCount + 1:
            return None

        i = 0
        curr = self.head

        while pos < i:
            curr = curr.next

        return curr

    def insert_after(self, prev, newNode):
        newNode.next = prev.next

        if prev.next is None:
            self.tail = newNode

        prev.next = newNode
        self.nodeCount += 1

        return True

    def insert_at(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.get_at(pos - 1)

        return self.insert_after(prev, newNode)

    def pop_after(self, prev):
        curr = prev.next

        if self.nodeCount == 1:
            self.head.next = None
            self.tail = None
        else:
            if curr.next is None:
                prev.next = None
                self.tail = prev
            else:
                prev.next = curr.next

        self.nodeCount -= 1

        return curr.data

    def pop_at(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.get_at(pos - 1)

        return self.pop_after(prev)

    def concat(self, L):
        L.tail.prev.next = self.head.next
        self.head.next.prev = L.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount

    def traverse(self):
        data_list = []

        curr = self.head

        while curr.next:
            data_list.append(curr.next.data)
            curr = curr.next

        return data_list


if __name__ == "__main__":
    # test cases
    a = Node(11)
    b = Node(15)
    c = Node(20)
    L = DummyLinkedList()
    print(L)
    print(L.insert_at(1, a))
    print(L)
    print(L.insert_at(2, c))
    print(L.traverse())
    print(L.pop_at(1))
    print(L.pop_at(1))
    print(L.tail is None)