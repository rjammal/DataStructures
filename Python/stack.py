class Stack:

    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def empty(self):
        return len(self.arr) == 0

    def __str__(self):
        return str([str(el) for el in self.arr])