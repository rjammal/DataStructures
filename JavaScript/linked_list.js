(function (root) {

function NoValuePresentError( message ) {
    this.message = message;
}

var SinglyLinkedList = root.SinglyLinkedList = function () {
    this.head = undefined;
    this.tail = undefined;
    this.length = 0;
}

SinglyLinkedList.Node = function (value) {
    this.value = value;
    this.next = undefined;
}

var singlyGetNode = function (index) {
    if (index >= this.length) {
        return undefined;
    }
    var current = this.head;
    var currentIndex = 0;
    while (currentIndex < index) {
        current = current.next;
        currentIndex++;
    }
    return current;
}

SinglyLinkedList.prototype.get = function (index) {
    var node = singlyGetNode.call(this, index);
    if (!node) {
        return undefined;
    }
    return node.value;
}

SinglyLinkedList.prototype.set = function (index, value) {
    var node = singlyGetNode.call(this, index);
    if (!node) {
        this.insert(index, value);
    } else {
        node.value = value;
    }
}

SinglyLinkedList.prototype.add = function (value) {
    var node = new SinglyLinkedList.Node(value);
    if (this.tail === undefined) {
        this.tail = node;
        this.head = node;
    } else {
        this.tail.next = node;
        this.tail = node;
    }
    this.length++;
}

SinglyLinkedList.prototype.insert = function (index, value) {
    var node = new SinglyLinkedList.Node(value);
    if (index === 0) {
        node.next = this.head;
        this.head = node;
        this.length++;
        return;
    }
    var current = this.head;
    var currentIndex = 0;
    while (currentIndex < index - 1) {
        if (!current) {
            this.add(undefined);
            current = this.head;
            continue;
        } 
        if (!current.next) {
            this.add(undefined);
        }
        current = current.next;
        currentIndex++;
    }
    node.next = current.next;
    current.next = node;
    if (current === this.tail) {
        this.tail = node;
    }
    this.length++;
}

SinglyLinkedList.prototype.remove = function (value) {
    var parent = undefined;
    var current = this.head;
    while (current) {
        if (current.value === value) {
            if (parent) {
                parent.next = current.next;
            } else {
                this.head = current.next;
            }
            if (!current.next) {
                this.tail = parent;
            }
            this.length--;
            return;
        } else {
            parent = current;
            current = current.next;
        }
    }
    throw new NoValuePresentError(value + " was not in the list.");
}


var DoublyLinkedList = root.DoublyLinkedList = function () {
    this.head = undefined;
    this.tail = undefined;
    this.length = 0;
}

DoublyLinkedList.Node = function (value) {
    this.value = value;
    this.next = undefined;
    this.prev = undefined;
}

DoublyLinkedList.prototype.add = function (value) {
    var node = new DoublyLinkedList.Node(value);
    if (this.head === undefined) {
        this.head = node;
        this.tail = node;
    } else {
        this.tail.next = node;
        node.prev = this.tail;
        this.tail = node;
    }
    this.length++;
}

var doublyGetNode = function (index) {
    if (this.length <= index) {
        return undefined;
    }
    var current = this.head;
    for (var i = 0; i < this.length; i++) {
        if (i === index) {
            return current;
        }
        current = current.next;
    }
}

DoublyLinkedList.prototype.get = function (index) {
    var node = doublyGetNode.call(this, index);
    if (!node) {
        return undefined;
    }
    return node.value;
}

DoublyLinkedList.prototype.set = function (index, value) {
    var node = doublyGetNode.call(this, index);
    if (!node) {
        this.insert(index, value);
    } else {
        node.value = value;
    }
}

DoublyLinkedList.prototype.insert = function (index, value) {
    var node = new DoublyLinkedList.Node(value);
    if (index === 0) {
        node.next = this.head;
        this.head = node;
        this.length++
        return;
    }
    var current = this.head;
    var currentIndex = 0;
    while (currentIndex < index - 1) {
        if (!current) {
            this.add(undefined);
            current = this.head;
            continue;
        }
        if (!current.next) {
            this.add(undefined);
        }
        current = current.next;
        currentIndex++;
    }
    node.prev = current;
    node.next = current.next;
    current.next = node;
    if (node.next) {
        node.next.prev = node;
    } else {
        this.tail = node;
    }
    this.length++;
}


DoublyLinkedList.prototype.remove = function (value) {
    var current = this.head;
    while (current) {
        if (current.value === value) {
            if (current.next) {
                current.next.prev = current.prev;
            } else {
                this.tail = current.prev;
            }
            if (current.prev) {
                current.prev.next = current.next;
            } else {
                this.head = current.next;
            }
            this.length--;
            return;
        } else {
            current = current.next;
        }
    }
    throw new NoValuePresentError(value + " was not in the list.");
}

QUnit.module("linked lists")

var linkedLists;

QUnit.testStart( function (details) {
    linkedLists = [new SinglyLinkedList(), new DoublyLinkedList()];
    linkedLists.forEach( function (list) { 
        list.add(5);
        list.add(3);
        list.add(4);
    })
});

QUnit.test("get", function (assert) {
    linkedLists.forEach( function (list) {
        assert.strictEqual(list.get(0), 5);
        assert.strictEqual(list.get(1), 3);
        assert.strictEqual(list.get(2), 4);
        assert.strictEqual(list.get(3), undefined);
    })
});

QUnit.test("insert", function (assert) {
    linkedLists.forEach( function (list) {
        list.insert(0, 10);
        assert.strictEqual(list.get(0), 10);
        assert.strictEqual(list.get(1), 5);
        assert.strictEqual(list.length, 4);
        list.insert(5, 6);
        assert.strictEqual(list.get(4), undefined);
        assert.strictEqual(list.get(5), 6);
        assert.strictEqual(list.length, 6)
    });
});

QUnit.test("set", function (assert) {
    linkedLists.forEach( function (list) {
        list.set(1, 7);
        assert.strictEqual(list.get(1), 7);
        list.set(5, 2);
        assert.strictEqual(list.length, 6);
        assert.strictEqual(list.get(5), 2);
        assert.strictEqual(list.get(3), undefined);
    });
});

QUnit.test("remove", function (assert) {
    linkedLists.forEach( function (list) {
        list.remove(3);
        assert.strictEqual(list.length, 2);
        assert.strictEqual(list.get(1), 4);
        list.remove(4);
        list.remove(5);
        assert.strictEqual(list.length, 0);
        assert.throws(
            function () { list.remove(2) }, 
            new NoValuePresentError("2 was not in the list.")
            );
    });
});

})(this);