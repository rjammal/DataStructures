class DynamicArray: 

    def __init__(self, size = 10):
        self.arr = [None] * size
        self.max = size
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
            self.max = max(self.max * 2, 10) # in case someone initializes with 0 or negative
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
        elif end < 0:
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