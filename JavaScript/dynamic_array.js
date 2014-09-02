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

DynamicArray.prototype.splice = function (index, len) {
    if (len === undefined) {
        len = this.length - index;
    }
    var result = new DynamicArray(len)
    var lengthAdjust = 0;
    for (var i = index; i < this.length; i++) {
        if (i < index + len) {
            result.push(this.get(i));
        }

        var replacementIndex = i + len;
        this.set(i, this.get(replacementIndex));
        if (replacementIndex >= this.length) {
            lengthAdjust++;
        } 
    }
    this.length -= lengthAdjust;
    return result;
}

DynamicArray.prototype.pop = function () {
    return this.splice(this.length - 1).get(0);
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

QUnit.test("splice", function (assert) {
    var newArr1 = arr.splice(0);
    assert.strictEqual(newArr1.get(0), 2);
    assert.strictEqual(newArr1.get(2), 10);
    assert.strictEqual(newArr1.get(4), undefined);
    assert.strictEqual(arr.length, 0);
    assert.strictEqual(newArr1.length, 4);
    
    var newArr2 = newArr1.splice(1, 2);
    assert.strictEqual(newArr1.get(0), 2);
    assert.strictEqual(newArr1.get(1), 6);
    assert.strictEqual(newArr1.length, 2);
    assert.strictEqual(newArr2.get(0), 7);
    assert.strictEqual(newArr2.get(1), 10);
    assert.strictEqual(newArr2.length, 2);

    var newArr3 = newArr1.splice(1, 12);
    assert.strictEqual(newArr3.length, 1);
    assert.strictEqual(newArr1.length, 1);
    assert.strictEqual(newArr3.get(0), 6);
});

QUnit.test("pop", function (assert) {
    assert.strictEqual(arr.pop(), 6);
    assert.strictEqual(arr.length, 3);
});

})(this);