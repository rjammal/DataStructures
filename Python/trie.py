import unittest
import string

# ALPHABET = list(string.ascii_lowercase)

class Trie:

    class Node:

        def __init__(self, char):
            self.value = char
            self.next_chars = []
            self.final = False
    
    def __init__(self):
        self.root = []

    def set(self, value):
        node_list = self.root
        for char in value:
            next_node_list = [node for node in node_list if node.value == char]
            if len(next_node_list) == 1:
                next_node = next_node_list[0]
                node_list = next_node.next_chars
            else:
                next_node = Trie.Node(char)
                node_list.append(next_node)
                node_list = next_node.next_chars
        next_node.final = True


    def get(self, value):
        result = []
        node_list = self.root
        current = None
        # navigate to end of value
        for char in value:
            # filter out child that matches char
            node_list = [node for node in node_list if node.value == char]
            # if nothing matched prefix, return
            if len(node_list) == 0:
                return result
            # all next children
            current = node_list[0]
            node_list = current.next_chars
        if current and current.final:
            result.append(value)
        for node in node_list:
            result.extend(Trie.get_words(node, value))
        return result


    def remove(self, value):
        if value == "":
            raise KeyError("You cannot remove the empty string.")

        node_list = self.root
        current = None
        parent = None
        for char in value:
            node_list = [node for node in node_list if node.value == char]
            if len(node_list) == 0:
                raise KeyError("That value is not in the Trie.")
            parent = current
            current = node_list[0]
            node_list = current.next_chars
        
        if len(current.next_chars) == 0:
            if parent:
                parent.next_chars.remove(current)
            else:
                self.root.remove(current)
        elif current.final:
            current.final = False
        else:
            raise KeyError("That value is not in the Trie.")


    @staticmethod
    def get_words(node, word_so_far):
        result = []
        word_so_far += node.value
        if node.final:
            result.append(word_so_far)
        for child in node.next_chars:
            result.extend(Trie.get_words(child, word_so_far))
        return result


class TestTrie(unittest.TestCase):
    
    def setUp(self):
        self.t = Trie()
        self.t.set("hello")
        self.t.set("he")
        self.t.set("help")
        self.t.set("tricycle")
        self.t.set("trip")
        self.t.set("test")
        self.t.set("bounce")

    def test_set(self):
        self.assertEqual(self.t.get("check"), [])
        self.t.set("check")
        self.assertEqual(self.t.get("check"), ["check"])

    def test_get(self):
        self.assertItemsEqual(self.t.get("hel"), ["hello", "help"])
        self.assertItemsEqual(self.t.get("t"), ["tricycle", "trip", "test"])
        self.assertItemsEqual(self.t.get(""), ["he", "hello", "help", "tricycle", "trip", "test", "bounce"])

    def test_remove(self):
        self.assertEqual(self.t.get("b"), ["bounce"])
        self.t.remove("bounce")
        self.assertEqual(self.t.get("b"), [])
        self.t.remove("tricycle")
        self.assertItemsEqual(self.t.get("t"), ["trip", "test"])
        self.t.remove("he")
        self.assertItemsEqual(self.t.get("he"), ["hello", "help"])
        self.assertRaises(KeyError, self.t.remove, "missing")


if __name__ == "__main__":
    unittest.main()