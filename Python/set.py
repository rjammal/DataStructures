import unittest
import hash as h

class Set:

    def __init__(self):
        self.hash = h.Hash()

    def add(self, el):
        self.hash.set(el, True)

    def remove(self, el):
        self.hash.delete(el)

    def contains(self, el):
        try:
            return self.hash.get(el)
        except KeyError:
            return False

class TestSet(unittest.TestCase):

    def setUp(self):
        self.s = Set()
        self.s.add(1)
        self.s.add(3)
        self.s.add("hi")

    def test_add(self):
        self.s.add(5)
        self.assertTrue(self.s.contains(5))

    def test_remove(self):
        self.assertTrue(self.s.contains(1))
        self.s.remove(1)
        self.assertFalse(self.s.contains(1))

    def test_contains(self):
        self.assertTrue(self.s.contains(3))
        self.assertFalse(self.s.contains(2))


if __name__ == "__main__":
    unittest.main()