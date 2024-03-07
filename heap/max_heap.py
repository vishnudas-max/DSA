class MaxHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._max_heapify(i, n)

    def _max_heapify(self, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._max_heapify(largest, n)

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def remove_max(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        max_val = self.heap[0]
        last_val = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_val
            self._max_heapify(0, len(self.heap))
        return max_val



max_heap = MaxHeap()
max_heap.build_heap([5,3,4,7,9,76,4,32,43])
print("\nMax heap:", max_heap.heap)
max_heap.insert(10)
print("Max heap after insert:", max_heap.heap)
print("Removed max element:", max_heap.remove_max())
print("Max heap after remove_max:", max_heap.heap)
