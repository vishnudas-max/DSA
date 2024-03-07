class MinHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):   # n //2 -1 can be used to find the last node with child or last internalnode
            self._min_heapify(i, n)

    def _min_heapify(self, i, n):
        smallest = i
        left = i * 2 + 1     # i * 2 +1 can be used to find the left child of the node
        right = i * 2 + 2    # i * 2 +2 can be used to find the right child of the node
 
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._min_heapify(smallest, n)

    def insert(self, val):

        """ (i-1) //2 can be used to find the parent of the node """


        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2



    def remove_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_val
            self._min_heapify(0, len(self.heap))
        return min_val


# Example usage
min_heap = MinHeap()
min_heap.build_heap([4, 1, 7, 3, 8, 5])
print("Min heap:", min_heap.heap)
min_heap.insert(2)
print("Min heap after insert:", min_heap.heap)
print("Removed min element:", min_heap.remove_min())
print("Min heap after remove_min:", min_heap.heap)
