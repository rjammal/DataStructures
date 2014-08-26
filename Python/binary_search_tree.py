import unittest
from random import shuffle

class BinarySearchTree:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def set(self, key, val):
        pass

    def get(self, key):
        pass

    def remove(self, key):
        pass

    def bfs(self, key):
        pass

    def dfs_in_order(self, key):
        pass

    def dfs_pre_order(self, key):
        pass

    def dfs_post_order(self, key):
        pass

    def find_node(self, key):
        pass


class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinarySearchTree()
        node_vals = list(range(9))
        shuffle(node_vals)
        for val in node_vals:
            self.bst.set(val, val)

    def test_search(self):
        self.bst.remove(5)
        tests = [
            (8, 8), 
            (10, None), 
            (5, None),
        ]

        for test in tests:
            # breadth first search
            self.assertEqual(self.bst.bfs(test[0]), test[1])

            # depth first search
            self.assertEqual(self.bst.dfs_in_order(test[0]), test[1])
            self.assertEqual(self.bst.dfs_pre_order(test[0]), test[1])
            self.assertEqual(self.bst.dfs_post_order(test[0]), test[1])
    
    def test_set(self):
        self.assertEqual(self.bst.get(4), 4)
        self.bst.set(4, 14)
        self.assertEqual(self.bst.get(4), 14)

    def test_get(self):
        self.assertEqual(self.bst.get(3), 3)
        self.assertRaises(KeyError, self.bst.get, 12)

    def test_remove(self):
        self.assertEqual(self.bst.get(4), 4)
        self.bst.remove(4)
        self.assertRaises(KeyError, self.bst.get, 4)

if __name__ == "__main__":
    unittest.main()