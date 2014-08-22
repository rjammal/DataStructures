import math

class Heap: 
    class Node: 
        def __init__(self, priority, value):
            self.priority = priority
            self.value = value

        def __str__(self):
            return str([self.priority, self.value])

    def __init__(self):
        self.arr = []

    def peek(self):
        return self.arr[0].value

    def push(self, priority, value):
        node = self.Node(priority, value)
        self.arr.append(node)
        current_index = len(self.arr) - 1
        while current_index > 0:
            parent_index = int(math.ceil(current_index / 2.0) - 1)
            current = self.arr[current_index]
            parent = self.arr[parent_index]
            if current.priority < parent.priority:
                self.arr[parent_index] = current
                self.arr[current_index] = parent
                current_index = parent_index
            else: # found its place
                break

    def pop(self):
        result = self.arr[0].value
        if len(self.arr) == 1:
            self.arr.pop()
            return result
        
        self.arr[0] = self.arr.pop()
        current_index = 0
        while current_index < len(self.arr):
            left_index = current_index * 2 + 1
            right_index = left_index + 1
            current = self.arr[current_index]
            left = None
            right = None
            if left_index < len(self.arr):
                left = self.arr[left_index]
            if right_index < len(self.arr):
                right = self.arr[right_index]

            # no children
            if not left and not right:
                break
            # only a left child or left is smaller than right
            # I do not need to consider the possibility of only a right child since that is
            # not a valid heap configuration
            elif not right or left.priority < right.priority:
                to_swap = left
                to_swap_i = left_index
            else: 
                to_swap = right
                to_swap_i = right_index

            if to_swap.priority < current.priority:
                self.arr[current_index] = to_swap
                self.arr[to_swap_i] = current
                current_index = to_swap_i
            else: 
                break
        return result

    def __str__(self):
        return str([str(x) for x in self.arr])