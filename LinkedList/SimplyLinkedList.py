class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0

    def __repr__(self):
        if self.nodeCount == 0:
            return "LinkedList is Empty!!"

        s = ""

        current = self.head
        while current is not None:
            s += repr(current.data)
            if current.next is not None:
                s += "->"
            current = current.next

        return s

    def get_length(self):
        return self.nodeCount

    def get_at(self, pos):
        """ Get target Position Node.

        :param pos: target position.
        :return: target position Node.
        """
        if pos <= 0 or pos > self.nodeCount:  # node 위치는 1번째 부터 시작.
            return None

        i = 1
        current = self.head

        while i < pos:
            current = current.next
            i += 1

        return current

    def insert_at(self, pos, newNode):
        """ Insert NewNode.

        :param pos: insert target position.
        :param newNode: insert newNode.
        :rtype: boolean.
        """
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if self.nodeCount == pos + 1:
                prev = self.tail
            else:
                prev = self.get_at(pos - 1)

            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1

        return True

    def delete_at(self, pos):
        data = 0

        if pos <= 0 or pos > self.nodeCount:
            raise IndexError

        if self.nodeCount == 1:
            data = self.head.data
            self.head = None
        else:
            prev = self.get_at(pos - 1)
            if pos == self.nodeCount:
                data = prev.next.data
                prev.next = None
                self.tail = prev
            else:
                data = prev.next.data
                prev.next = prev.next.next

        if self.nodeCount == 1:
            self.head = None
            self.tail = None

        self.nodeCount -= 1

        return data

    def concat(self, L):
        """ Concat Other LinkedList.

        :param L: Other LinkedList
        :return: Concated LinkedList
        :rtype: LinkedList
        """
        self.tail.next = L.head

        if L.tail:
            self.tail = L.tail

        self.nodeCount += L.nodeCount

    def traverse(self):
        data_list = []

        current = self.head

        while current is not None:
            data_list += [current.data]
            current = current.next

        return data_list