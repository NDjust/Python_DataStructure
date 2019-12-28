class Queue:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        data = self.data[0]
        self.data = self.data[1:]

        return data

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"

        return self.data[0]

