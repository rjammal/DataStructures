(function () {

function SinglyLinkedList() {
    this.head = undefined;
    this.tail = undefined;
    this.length = 0;
}

SinglyLinkedList.Node = function (value) {
    this.value = value;
    this.next = undefined;
}

SinglyLinkedList.prototype.get = function (index) {
    if (index >= this.length) {
        return undefined;
    }
    var current = this.head;
    var currentIndex = 0;
    while (currentIndex < index) {
        current = current.next;
        currentIndex++;
    }
    return current.value;
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


function DoublyLinkedList() {
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

DoublyLinkedList.prototype.get = function (index) {
    if (this.length <= index) {
        return undefined;
    }
    var current = this.head;
    for (var i = 0; i < this.length; i++) {
        if (i === index) {
            return current.value;
        }
        current = current.next;
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
})

})();