class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is Empty!!"

        data = self.data[-1]
        self.data = self.data[:-1]
        return data

    def peek(self):
        if self.is_empty():
            return "Stack is Empty!!"

        return self.data[-1]
