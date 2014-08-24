import unittest

class DynamicArray: 

    def __init__(self, size = 10):
        self.arr = [None] * size
        self.max = max(size, 1)
        self.length = 0

    def get(self, i):
        self.check_index(i)
        if i < 0:
            i += self.length
        return self.arr[i]

    def set(self, i, value): 
        self.check_index(i)
        if i < 0:
            i += self.length
        self.arr[i] = value

    def push(self, value): 
        if self.length >= self.max:
            self.max *= 2 # in case someone initializes with 0 or negative
            new_arr = [None] * self.max
            for i in range(self.length):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

        self.arr[self.length] = value
        self.length += 1

    def pop(self, i = -1):
        self.check_index(i)
        if i < 0: 
            i += self.length # convert to positive

        result = self.arr[i]

        if i < self.length - 1: # if i is last element, only need to reduce length
            for idx in range(i, self.length):
                self.arr[idx] = self.arr[idx + 1]
        self.length -= 1

        # free up space if length is 1/4 max
        if self.length <= self.max / 4:
            self.max = max(self.max // 2, 10)
        new_arr = [None] * self.max
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

        return result

    def slice(self, start = 0, end = None):
        self.check_index(start)
        if start < 0: 
            start += self.length
        
        if end == None:
            end = self.length
        if end < 0:
            end += self.length

        # cannot use check_index because the end point is not included, so self.length is valid
        if end > self.length or end < 0: 
            raise IndexError("End is out of range.")

        result = DynamicArray(end - start)

        for i in range(start, end): 
            result.push(self.arr[i])

        return result

    def __str__(self):
        if self.length == 0:
            return str([])
        else:
            result = self.slice(0, self.length)
            return str(result.arr)

    def check_index(self, i):
        if i >= self.length or i < -self.length:
            raise IndexError("Array index out of range.")


class TestDynamicArray(unittest.TestCase):

    def setUp(self):
        self.d = DynamicArray(4)
        self.d.push(1)
        self.d.push(5)
        self.d.push(2)
        self.d.push(9)
        self.d.push(4)

    def test_get(self):
        self.assertEqual(self.d.get(0), 1)
        self.assertEqual(self.d.get(2), 2)
        self.assertEqual(self.d.get(-2), 9)
        self.assertRaises(IndexError, self.d.get, 10)
        self.assertRaises(IndexError, self.d.get, -6)

    def test_set(self):
        self.d.set(0, 5)
        self.assertEqual(self.d.get(0), 5)
        self.d.set(-1, 6)
        self.assertEqual(self.d.get(-1), 6)
        self.assertRaises(IndexError, self.d.set, 5, 1)
        self.assertRaises(IndexError, self.d.set, -15, 1)

    def test_push(self):
        self.assertEqual(self.d.max, 8)

        length = self.d.length
        self.d.push(3)
        self.assertEqual(self.d.length, length + 1)
        self.assertEqual(self.d.get(-1), 3)

    def test_pop(self):
        length = self.d.length
        self.assertEqual(self.d.pop(3), 9)
        self.assertEqual(self.d.length, length - 1)
        self.assertEqual(self.d.pop(), 4)

    def test_slice(self):
        length = self.d.length
        self.assertEqual(length, self.d.slice().length)
        
        d_slice = self.d.slice(2)
        self.assertEqual(d_slice.get(0), 2)
        self.assertEqual(d_slice.get(-1), 4)
        self.assertEqual(d_slice.length, 3)

        d_slice = self.d.slice(1, 3)
        self.assertEqual(d_slice.get(0), 5)
        self.assertEqual(d_slice.get(-1), 2)
        self.assertEqual(d_slice.length, 2)

if __name__ == "__main__":
    unittest.main()