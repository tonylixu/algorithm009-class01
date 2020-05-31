class MinBinaryHeap():
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, v):
        """Insert value v to BinaryHeap"""
        # Insert at the end
        self.heap_list.append(v)
        self.size += 1
        self.heapifyup(self.size)

    def heapifyup(self, i):
        """Place the given element i to the right order"""
        parent = i//2
        while parent != 0:
            if self.heap_list[i] < self.heap_list[parent]:
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
            parent //= 2

    def min_child(self, i):
        """For a given node i, return its min child"""
        # Check if the given node has two children
        if i*2*2 > self.size:
            return i*2+1
        else:
            if self.heap_list[i*2+1] < self.heap_list[i*2+2]:
                return i*2+1
            else:
                return i*2+2

    def del_min(self):
        """Delete the minimum elment, usually root"""
        root_value = self.heap_list[0]
        # Assign last element to rool
        self.heap_list[0] = self.heap_list[self.size-1]
        self.size -= 1
        self.heap_list.pop()
        self.heapifydown(0)

    def heapifydown(self, i):
        """We need to check all the children of position i, before we can determine where to
        put it at the right place
        """
        while i*2+2 <= self.size:
            min_child = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def build_binary_heap(self, a_list):
        """To build from a list, we start from the middle"""
        i = len(a_list)//2
        print(i)
        self.size = len(a_list)
        self.heap_list = a_list
        while i >= 0:
            self.heapifydown(i)
            i -= 1


s = [9, 5, 5, 6, 2, 3]
s = [3, 9, 1, 14, 8, 7]
b_heap = MinBinaryHeap()
b_heap.build_binary_heap(s)
print(b_heap.heap_list)
