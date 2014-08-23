import linked_list as ll

class Queue:

    def __init__(self):
        self.data = ll.DoublyLinkedList()

    def enqueue(self, value):
        self.data.push(value)

    def dequeue(self):
        return self.data.pop(0)

    def empty(self):
        return self.data.length == 0

    def __str__(self):
        return str(self.data)