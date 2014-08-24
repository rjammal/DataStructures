import unittest

class SinglyLinkedList: 

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value): 
        node = self.Node(value)
        if not self.head: 
            self.head = node
        else: 
            current = self.head
            while current.next:
                current = current.next
            current.next = node

        self.length += 1

    def pop(self, i = None):
        # set default
        if i == None:
            i = self.length - 1

        self.check_index(i)

        if i < 0:
            i += self.length

        if i == 0:
            result = self.head
            self.head = self.head.next
            self.length -= 1
            return result.value

        counter = 1
        parent = self.head
        current = self.head.next
        while counter < i:
            parent = current
            current = current.next
            counter += 1
        parent.next = current.next
        self.length -= 1
        return current.value

    def get(self, i): 
        node = self.find_node(i)
        return node.value

    def set(self, i, value): 
        node = self.find_node(i)
        node.value = value

    def find_node(self, i):
        self.check_index(i)
        if i < 0:
            i += self.length

        current = self.head
        counter = 0
        while counter < i:
            current = current.next
            counter += 1
        return current

    def size(self): 
        return self.length

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return "[" + ", ".join(result) + "]"

    def check_index(self, i):
        if i < -self.length or i >= self.length:
            raise IndexError("Index out of bounds.")

class DoublyLinkedList:

    class Node:
        def __init__(self, value): 
            self.value = value
            self.next = None
            self.prev = None

        def __str__(self):
            return str(self.value)

    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = self.Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop(self, i = None):
        if i == None: 
            i = self.length - 1

        self.check_index(i)
        if i < 0:
            i += self.length

        current = self.head
        counter = 0
        while counter < i:
            current = current.next
            counter += 1
        if current.prev: 
            current.prev.next = current.next
        else: 
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else: 
            self.tail = current.prev

        self.length -= 1
        return current.value

    def get(self, i):
        node = self.find_node(i)
        return node.value

    def set(self, i, value):
        node = self.find_node(i)
        node.value = value

    def size(self):
        return self.length

    def __str__(self): 
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return "[" + ", ".join(result) + "]"

    def find_node(self, i):
        self.check_index(i)
        if i < 0:
            i += self.length

        current = self.head
        counter = 0
        while counter < i:
            current = current.next
            counter += 1
        return current

    def check_index(self, i):
        if i < -self.length or i >= self.length:
            raise IndexError("Index out of bounds.")

class TestLinkedList(unittest.TestCase):

    def setUp(self): 
        self.lists = [SinglyLinkedList(), DoublyLinkedList()]
        for l in self.lists:
            l.push(5)
            l.push(6)
            l.push(2)
            l.push(7)

    def test_pop(self):
        for l in self.lists:
            size = l.size()
            self.assertEqual(l.pop(), 7)
            self.assertEqual(l.size(), size - 1)
            self.assertEqual(l.pop(1), 6)

    def test_push(self):
        for l in self.lists:
            size = l.size()
            l.push(10)
            self.assertEqual(l.size(), size + 1)
            self.assertEqual(l.get(-1), 10)

    def test_get(self):
        for l in self.lists:
            self.assertEqual(l.get(0), 5)
            self.assertEqual(l.get(-2), 2)
            self.assertRaises(IndexError, l.get, 4)
            self.assertRaises(IndexError, l.get, -5)

    def test_set(self):
        for l in self.lists:
            size = l.size()
            l.set(0, 3)
            self.assertEqual(l.get(0), 3)
            l.set(-2, 10)
            self.assertEqual(l.get(-2), 10)
            self.assertEqual(l.size(), size)
            self.assertRaises(IndexError, l.set, 4, 1)
            self.assertRaises(IndexError, l.set, -5, 1)

if __name__ == "__main__":
    unittest.main()