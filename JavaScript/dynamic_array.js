(function (root) {

var DynamicArray = root.DynamicArray = function (len) {
    len = Math.max(len, 1);
    len = len || 1;
    this.arr = new Array(len);
    this.max = len;
    this.length = 0;
}

var resize = function () {
    var newArr = new Array(this.max);
    for (var i = 0; i < this.length; i++) {
        newArr[i] = this.arr[i];
    }
    this.arr = newArr;
}

DynamicArray.prototype.push = function (value) {
    if (this.length >= this.max) {
        this.max *= 2;
        resize.call(this);
    }
    this.arr[this.length++] = value;
}

DynamicArray.prototype.get = function (index) {
    return this.arr[index];
}

DynamicArray.prototype.set = function (index, value) {
    if (this.max < index) {
        this.max = index * 2;
        resize.call(this);
    }
    if (index >= this.length) {
        this.length = index + 1;
    }
    this.arr[index] = value;
}

QUnit.module("dynamic array");

var arr;

QUnit.testStart( function () {
    arr = new DynamicArray(3)
    arr.push(2);
    arr.push(7);
    arr.push(10);
    arr.push(6);
});

QUnit.test("get", function (assert) {
    assert.strictEqual(arr.get(0), 2);
    assert.strictEqual(arr.get(3), 6);
    assert.strictEqual(arr.get(7), undefined);
});

QUnit.test("set", function (assert) {
    arr.set(1, 9);
    assert.strictEqual(arr.get(1), 9);
    assert.strictEqual(arr.length, 4);
    arr.set(10, 5);
    assert.strictEqual(arr.length, 11);
    assert.strictEqual(arr.get(4), undefined);
    assert.strictEqual(arr.get(10), 5);
});

})(this);