(function (root) {

var Graph = root.Graph = function () {
    this.vertices = new root.DynamicArray();
}

Graph.Vertex = function (value) {
    this.value = value;
    this.edges = new root.DynamicArray();
}

Graph.Vertex.prototype.toString = function () {
    return this.value;
}

var indexOfVertexValue = function (value) {
    for (var i = 0; i < this.vertices.length; i++) {
        if (this.vertices.get(i).value === value) {
            return i;
        }
    }
    return -1;
}

var findVertex = function (value) {
    return this.vertices.find( function (el) {
        return el.value === value;
    });
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
    var vert1 = findVertex.call(this, val1);
    var vert2 = findVertex.call(this, val2);
    if (!vert1 || !vert2) {
        throw new NotPresentError("Both vertices must be in the graph.");
    }
    vert1.edges.push({vertex: vert2, weight: weight});
}

Graph.prototype.connected = function (val1, val2) {
    var vert1 = findVertex.call(this, val1);
    if (!vert1) {
        throw new NotPresentError(val1 + " is not in the graph.");
    }
    var result = vert1.edges.find( function (el) {
        return el.vertex.value === val2;
    });
    return !!result;
}

Graph.prototype.shortestPath = function (val1, val2) {
    var result;
    var heap = new root.Heap();
    var start = findVertex.call(this, val1);
    if (!start) {
        throw new NotPresentError("Starting location must be on the graph.")
    }
    start.distance = 0;
    heap.add(0, start);
    while (!heap.isEmpty()) {
        var current = heap.pop();
        current.done = true;
        if (current.value === val2) {
            return processSolution.call(this, current);
        }
        current.edges.forEach( function (edge) {
            var vertex = edge.vertex;
            if (vertex.done) {
                return;
            }
            if (!vertex.distance || vertex.distance > edge.weight + current.distance) {
                vertex.distance = edge.weight + current.distance;
                vertex.parent = current;
            }
            heap.add(vertex.distance, vertex);
        });
    }
    cleanUp.call(this);
    return {path: [], distance: null};
}

var processSolution = function (vertex) {
    var result = {path: [], distance: vertex.distance};
    while (vertex) {
        result.path.push(vertex.value);
        vertex = vertex.parent;
    }
    result.path.reverse();
    cleanUp.call(this);
    return result;
}

var cleanUp = function () {
    this.vertices.forEach( function (v) {
        delete v.parent;
        delete v.distance;
        delete v.done;
    });
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
    graph.addEdge(4, 1, 2);
    graph.addEdge(4, 3, 5);
});

QUnit.test("connected", function (assert) {
    assert.ok(graph.connected(2, 4));
    assert.ok(graph.connected(1, 3));
    assert.ok(!graph.connected(4, 2));
    assert.throws(
        graph.connected.bind(graph, 9, 1), 
        NotPresentError
        )
});

QUnit.test("shortestPath", function (assert) {
    assert.deepEqual(graph.shortestPath(2, 4), {path: [2, 4], distance: 5});
    assert.deepEqual(graph.shortestPath(2, 1), {path: [2, 4, 1], distance: 7});
    assert.deepEqual(graph.shortestPath(2, 3), {path: [2, 4, 1, 3], distance: 8});
    assert.deepEqual(graph.shortestPath(1, 2), {path: [], distance: null});
});

})(this);