import unittest

class DisjointSet:

    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0

    def find_parent(self):
        if self.parent != self:
            self.parent = self.parent.find_parent()
        return self.parent

    def union(self, other): 
        if self.find_parent() == other.find_parent():
            return

        if self.rank < other.rank:
            self.parent = other.parent
        elif self.rank > other.rank:
            other.parent = self.parent
        else:
            other.parent = self.parent
            self.rank += 1


class TestDisjointSet(unittest.TestCase):

    def setUp(self):
        self.d1 = DisjointSet(1)
        self.d2 = DisjointSet(2)
        self.d3 = DisjointSet(3)

    def test_find_parent(self):
        self.assertEqual(self.d1.find_parent(), self.d1)
        self.assertNotEqual(self.d1.find_parent(), self.d2.parent)

    def test_union(self):
        self.d1.union(self.d2)
        self.assertEqual(self.d1.find_parent(), self.d2.find_parent())
        self.d3.union(self.d1)
        self.assertEqual(self.d2.find_parent(), self.d3.find_parent())



if __name__ == "__main__":
    unittest.main()