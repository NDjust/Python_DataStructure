class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.nodeCount = 0

    def __repr__(self):
        if self.nodeCount == 0:
            return "LinkedList is Empty!"

        i = 0
        s = ""
        current = self.head

        while i < self.nodeCount:
            s += str(current.data)

            if i < self.nodeCount - 1:
                s += " -> "
            i += 1

            current = current.next

        return s

    def get_length(self):
        return self.nodeCount

    def get_at(self, pos):
        """  Get Target Position Node.

        :param pos: Target Position.
        :rtype: Node
        """
        if pos <= 0 or pos > self.nodeCount + 1:
            return None

        i = 1
        current = self.head

        while i < pos:
            current = current.next
            i += 1

        return current

    def insert_at(self, pos, newNode):
        if pos <= 0 or pos > self.nodeCount + 1:
            return False

        if pos == 1 and self.nodeCount == 0:
            newNode.next = self.head
            self.head = newNode
            self.nodeCount += 1
            return True

        if pos == 1 and self.nodeCount + 1 != pos:  # Insert First node.
            newNode.next = self.head
            self.head = newNode
        else:
            prev = self.get_at(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        self.nodeCount += 1

        return True

    def delete_at(self, pos):
        data = 0

        if pos <= 0 or pos > self.nodeCount:
            raise IndexError

        if pos == 1 and self.nodeCount + 1 == pos:
            data = self.head.data
            self.head = None
        else:
            prev = self.get_at(pos - 1)
            data = prev.next.data
            prev.next = prev.next.next

        self.nodeCount -= 1

        return data

    def traverse(self):
        data_list = []

        current = self.head
        i = 0

        while i < self.nodeCount:
            data_list.append(current.data)
            current = current.next
            i += 1

        return data_list


if __name__ == "__main__":
    node1 = Node(33)
    node2 = Node(11)
    node3 = Node(22)
    node4 = Node(55)
    node5 = Node(44)

    CL = CircularLinkedList()
    CL.insert_at(1, node1)
    CL.insert_at(2, node2)
    CL.insert_at(1, node3)
    print(CL)

    CL.delete_at(2)
    print(CL)

    CL.insert_at(2, node4)
    CL.insert_at(3, node5)

    print(CL)
    print(CL.traverse())
