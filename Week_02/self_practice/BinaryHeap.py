class BinaryHeap():
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def heapifyup(self, i):
        """heapifyup the inserted element to the right place in the binary heap"""
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i //= 2

    def insert(self, v):
        """Insert a new element v into binary heap"""
        self.heap_list.append(v)
        self.size += 1
        self.heapifyup(self.size)

    def heapifydown(self, i):
        """Heapifydown the given element to the right place in the binary heap"""
        while i*2+2 <= self.size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        """Return the minimum child value of node i"""
        # If node i has only one leaf, return the leaf
        if i*2+2 > self.size:
            return i*2+1
        else:
            if self.heap_list[i*2+1] < self.heap_list[i*2+2]:
                return i*2+1
            else:
                return i*2+2

    def del_min(self):
        """Remove the node that has the minimum value, since the minimum element is
        always at index 0 of minimum heap, we delete [0]
        """
        root_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.size-1]
        self.size -= 1
        self.heap_list.pop()
        self.heapifydown(0)
        return root_val

    def build_binary_heap(self, a_list):
        i = len(a_list)//2
        self.size = len(a_list)
        self.heap_list = a_list
        while i >= 0:
            self.heapifydown(i)
            i -= 1


s = [9, 5, 6, 2, 3]
b_heap = BinaryHeap()
b_heap.build_binary_heap(s)
print(b_heap.heap_list)