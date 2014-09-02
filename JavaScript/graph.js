(function (root) {

var Graph = root.Graph = function () {
    this.vertices = new root.DynamicArray();
}

Graph.Vertex = function (value) {
    this.value = value;
    this.edges = {};
}

Graph.Vertex.prototype.toString = function () {
    var edgesArr = [];
    for (var e in this.edges) {
        if (this.edges.hasOwnProperty(e)) {
            edgesArr.push(e);
        }
    }
    var currentVertex = this;
    edgesArr = edgesArr.map( function (vert) {
        return "(" + vert + ", " + currentVertex.edges[vert] + ")"
    });
    return this.value + ": " + edgesArr.join(", ");
}

var indexOfVertexValue = function (value) {
    for (var i = 0; i < this.vertices.length; i++) {
        if (this.vertices.get(i).value === value) {
            return i;
        }
    }
    return -1;
}

function AlreadyPresentError(message) {
    this.message = message;
}

function NotPresentError(message) {
    this.message = message;
}

Graph.prototype.addVertex = function (value) {
    if (indexOfVertexValue.call(this, value) >= 0) {
        throw new AlreadyPresentError("That vertex is already in the graph.");
    }
    this.vertices.push(new Graph.Vertex(value));
}

Graph.prototype.addEdge = function (val1, val2, weight) {
    var val1Index = indexOfVertexValue.call(this, val1);
    var val2Index = indexOfVertexValue.call(this, val2);
    if (val1Index < 0 || val2Index < 0) {
        throw new NotPresentError("Both vertices must be in the graph.");
    }
    var v1 = this.vertices.get(val1Index);
    v1.edges[val2] = weight;
}

Graph.prototype.connected = function (val1, val2) {
    var val1Index = indexOfVertexValue.call(this, val1);
    if (val1Index < 0) {
        throw new NotPresentError(val1 + " is not in the graph.");
    }
    var vert1 = this.vertices.get(val1Index);
    return !!vert1.edges[val2];
}

QUnit.module("graphs");

var graph;

QUnit.testStart(function () {
    graph = new Graph();
    graph.addVertex(2);
    graph.addVertex(4);
    graph.addVertex(1);
    graph.addVertex(7);
    graph.addVertex(3);
    graph.addEdge(2, 4, 5);
    graph.addEdge(7, 1, 2);
    graph.addEdge(1, 3, 1);
    graph.addEdge(4, 1, 5);
});

QUnit.test("connected", function (assert) {
    assert.ok(graph.connected(2, 4));
    assert.ok(graph.connected(1, 3));
    assert.ok(!graph.connected(4,2));
    assert.throws(
        graph.connected.bind(graph, 9, 1), 
        NotPresentError
        )
});

})(this);