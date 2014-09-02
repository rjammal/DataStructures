(function (root) {

var Heap = root.Heap = function () {
    this.arr = new root.DynamicArray();
}

function Node(priority, value) {
    this.priority = priority;
    this.value = value;
}

Heap.prototype.add = function (priority, value) {
    var node = new Node(priority, value);
    this.arr.push(node);
    var index = this.arr.length - 1;
    while (index > 0) {
        var parentIndex = Math.floor((index - 1) / 2);
        if (this.arr.get(index).priority < this.arr.get(parentIndex).priority) {
            var temp = this.arr.get(index);
            this.arr.set(index, this.arr.get(parentIndex));
            this.arr.set(parentIndex, temp);
            index = parentIndex;
        } else {
            break;
        }
    }
}

Heap.prototype.pop = function () {
    var result = this.arr.get(0);
    this.arr.set(0, this.arr.get(this.arr.length - 1));
    var index = 0;
    this.arr.pop();
    while (index < this.arr.length) {
        var child1 = index * 2 + 1;
        var child2 = index * 2 + 2;
        var smallestChild;
        if (child1 >= this.arr.length) {
            return result.value;
        }
        if (child2 >= this.arr.length || this.arr.get(child1).priority < this.arr.get(child2).priority) {
            smallestChild = child1;
        } else {
            smallestChild = child2;
        }
        if (this.arr.get(index).priority > this.arr.get(smallestChild).priority) {
            var temp = this.arr.get(index);
            this.arr.set(index, this.arr.get(smallestChild));
            this.arr.set(smallestChild, temp);
            index = smallestChild;
        } else {
            break;
        }
    }
    return result.value;
}

Heap.prototype.isEmpty = function () {
    return this.arr.length === 0;
}

QUnit.module("heap");

var heap;

QUnit.testStart( function () {
    heap = new Heap();
    heap.add(4, 4);
    heap.add(5, 5);
    heap.add(2, 2);
    heap.add(7, 7);
    heap.add(1, 1);
});

QUnit.test("pop and isEmpty", function (assert) {
    assert.strictEqual(heap.pop(), 1);
    assert.strictEqual(heap.pop(), 2);
    assert.strictEqual(heap.pop(), 4);
    assert.strictEqual(heap.pop(), 5);
    assert.ok(!heap.isEmpty());
    assert.strictEqual(heap.pop(), 7);
    assert.ok(heap.isEmpty());
})

})(this);