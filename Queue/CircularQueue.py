class LinkedQueue:

    def __init__(self, n):
        self.max_count = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def is_full(self):
        return None not in self.data

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full!")

        self.rear = (self.rear + 1) % (self.max_count)
        self.data[self.rear] = item
        self.count += 1

        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")

        data = self.data[self.front]
        self.front = (self.front + 1) % (self.max_count)
        self.count -= 1

        return data

    def peek(self):
        if self.is_empty():
            return "Queue is Empty!"

        return self.data[(self.front + 1) % (self.max_count)]