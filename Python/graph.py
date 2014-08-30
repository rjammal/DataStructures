import unittest

class GraphList:
    
    class Vertex:
        def __init__(self, value):
            self.value = value
            self.edges = {}

    def __init__(self):
        self.vertices = []

    def add_vertex(self, value):
        self.vertices.append(GraphList.Vertex(value))

    def add_edge(self, v1, v2, weight = 1):
        vertices = [vertex for vertex in self.vertices if vertex.value == v1 or vertex.value == v2]
        if len(vertices) < 2:
            raise ValueError("Please select an existing vertex.")
        for v in vertices:
            if v.value == v1:
                vertex1 = v
            else:
                vertex2 = v
        if vertex2 in vertex1.edges or vertex1 in vertex2.edges:
            raise ValueError("Edge already exists.")

        vertex1.edges[vertex2] = weight
        vertex2.edges[vertex1] = weight

    def connected(self, val1, val2):
        for v in self.vertices:
            if v.value == val1:
                return val2 in [vertex.value for vertex in v.edges.keys()]
            elif v.value == val2:
                return val1 in [vertex.value for vertex in v.edges.keys()]
        return False


class DirectedGraphList:
    class Vertex:
        def __init__(self, value):
            self.value = value
            self.edges = {}

    def __init__(self):
        self.vertices = []

    def add_vertex(self, value):
        self.vertices.append(GraphList.Vertex(value))

    def add_edge(self, v1, v2, weight = 1):
        vertices = [vertex for vertex in self.vertices if vertex.value == v1 or vertex.value == v2]
        if len(vertices) < 2:
            raise ValueError("Please select an existing vertex.")
        for v in vertices:
            if v.value == v1:
                vertex1 = v
            else:
                vertex2 = v
        if vertex2 in vertex1.edges:
            raise ValueError("Edge already exists.")

        vertex1.edges[vertex2] = weight

    def connected(self, val1, val2):
        for v in self.vertices:
            if v.value == val1:
                return val2 in [vertex.value for vertex in v.edges]
        return False


class GraphMatrix:
    
    def __init__(self):
        self.matrix = []
        # keep track of indices
        self.vertices = []

    def add_vertex(self, value):
        self.matrix.append([None] * len(self.vertices))
        for row in self.matrix:
            row.append(None)
        self.vertices.append(value)

    def add_edge(self, v1, v2, weight = 1):
        try:
            v1_index = self.vertices.index(v1)
            v2_index = self.vertices.index(v2)
        except ValueError:
            raise ValueError("Please select an existing vertex.")
        self.matrix[v1_index][v2_index] = weight
        self.matrix[v2_index][v1_index] = weight

    def connected(self, v1, v2):
        try:
            v1_index = self.vertices.index(v1)
            v2_index = self.vertices.index(v2)
        except ValueError:
            raise ValueError("Please select an existing vertex.")
        return not self.matrix[v1_index][v2_index] is None


class DirectedGraphMatrix:
    def __init__(self):
        self.matrix = []
        # keep track of indices
        self.vertices = []

    def add_vertex(self, value):
        self.matrix.append([None] * len(self.vertices))
        for row in self.matrix:
            row.append(None)
        self.vertices.append(value)

    def add_edge(self, v1, v2, weight = 1):
        try:
            v1_index = self.vertices.index(v1)
            v2_index = self.vertices.index(v2)
        except ValueError:
            raise ValueError("Please select an existing vertex.")
        self.matrix[v1_index][v2_index] = weight

    def connected(self, v1, v2):
        try:
            v1_index = self.vertices.index(v1)
            v2_index = self.vertices.index(v2)
        except ValueError:
            raise ValueError("Please select an existing vertex.")
        return not self.matrix[v1_index][v2_index] is None

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graphs = [GraphList(), GraphMatrix()]
        self.directed_graphs = [DirectedGraphList(), DirectedGraphMatrix()]

        for g in self.graphs + self.directed_graphs:
            g.add_vertex("a")
            g.add_vertex("b")
            g.add_vertex("c")
            g.add_vertex("d")
            g.add_vertex("e")
            g.add_edge("a", "b", 3)
            g.add_edge("a", "d", 2)
            g.add_edge("a", "c", 6)
            g.add_edge("c", "b", 2)
            g.add_edge("d", "b", 1)

    def test_connected(self):
        for g in self.graphs + self.directed_graphs:
            self.assertTrue(g.connected("a", "b"))
            self.assertFalse(g.connected("c", "e"))
            self.assertFalse(g.connected("a", "e"))
            g.add_edge("a", "e")
            self.assertTrue(g.connected("a", "e"))

        for g in self.graphs:
            self.assertTrue(g.connected("e", "a"))

        for g in self.directed_graphs:
            self.assertFalse(g.connected("e", "a"))
            g.add_edge("e", "a")
            self.assertTrue(g.connected("e", "a"))

if __name__ == "__main__":
    unittest.main()