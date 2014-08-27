import unittest
from random import shuffle

class BinarySearchTree:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def set(self, key, value):
        if not self.root:
            self.root = BinarySearchTree.Node(key, value)
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTree.Node(key, value)
                    return
            elif key > current.key:
                if current.right:
                    current = current.right
                else:
                    current.right = BinarySearchTree.Node(key, value)
                    return
            else: 
                current.value = value
                return


    def get(self, key):
        current = self.root

        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else: 
                return current.value

        raise KeyError("Key not present.")

    def remove(self, key):
        if not self.root:
            raise KeyError("Key not present.")
        if self.root.key == key:
            if self.root.left == None:
                self.root = self.root.right
            elif self.root.right == None:
                self.root = self.root.left
            else:
                parent = self.root
                current = self.root.left
                while current.right: 
                    parent = current
                    current = current.right

                if parent == self.root:
                    parent.left = current.left
                else:
                    parent.right = current.left
                current.left = self.root.left
                current.right = self.root.right
                self.root = current
            return
        
        parent = self.root
        current = self.root
        while current: 
            if current.key > key:
                parent = current
                current = current.left
                continue
            elif current.key < key:
                parent = current
                current = current.right
                continue

            if current.right == None: 
                if parent.left == current:
                    parent.left = current.left
                else: 
                    parent.right = current.left
                return
            if current.left == None: 
                if parent.left == current:
                    parent.left == current.right
                else:
                    parent.right == current.right
                return

            largest_child_parent = current
            largest_child = current.left
            while largest_child.right:
                largest_child_parent = largest_child
                largest_child = largest_child.right
            if largest_child_parent == parent:
                parent.left = largest_child.left
            else:
                largest_child_parent.right = largest_child.left

            current.key = largest_child.key
            current.value = largest_child.value
            return

        raise KeyError("Key not present.")



    def bfs(self, value):
        pass

    def dfs_in_order(self, value):
        pass

    def dfs_pre_order(self, value):
        pass

    def dfs_post_order(self, value):
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