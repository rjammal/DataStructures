class Hash:

    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.key) + ":" + str(self.value)

    def __init__(self, space = 10):
        self.arr = [None] * space
        self.size = 0
        self.space = max(1, space)

    def set(self, key, value):
        node = self.Node(key, value)
        key_index = hash(key) % self.space

        Hash.insert_node(node, self.arr, key_index)

        self.size += 1

        # resize
        if self.size >= self.space: 
            self.space *= 2
            new_arr = [None] * self.space
            for i in range(len(self.arr)):
                current = self.arr[i]
                while current: 
                    key_index = hash(current.key) % self.space
                    Hash.insert_node(current, new_arr, key_index)
                    current = current.next
            self.arr = new_arr


    def get(self, key): 
        i = hash(key) % self.space
        current = self.arr[i]
        while current: 
            if current.key == key:
                return current.value
            else: 
                current = current.next

        raise KeyError("Given key is not present.") 

    def __str__(self):
        nodes = []
        for spot in self.arr:
            while spot: 
                nodes.append(spot)
                spot = spot.next
        return str([str(node) for node in nodes])

    @staticmethod
    def insert_node(node, arr, i):
        if not arr[i]:
            arr[i] = node
            return
        current = arr[i]
        while current.key != node.key and current.next:
            current = current.next
        if current.key == node.key:
            current.value = node.value
        else: 
            current.next = node
