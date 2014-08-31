(function () {

function SinglyLinkedList() {
    this.head = undefined;
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
    var currentIndex = this.length - 1;
    while (current && currentIndex > index) {
        current = current.next;
        currentIndex--;
    }
    if (current === undefined) {
        return undefined;
    } else {
        return current.value;
    }
}

SinglyLinkedList.prototype.add = function (value) {
    var node = new SinglyLinkedList.Node(value);
    node.next = this.head;
    this.head = node;
    this.length++;
}


function DoublyLinkedList() {
    this.head = undefined;
    this.length = 0;
}


var linkedLists;

QUnit.testStart( function (details) {
    linkedLists = [new SinglyLinkedList()]; //, new DoublyLinkedList()
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

})();