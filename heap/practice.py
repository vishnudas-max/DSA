class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self,i,n):
        largest = i
        left = i *2 +1
        right = i *2 +2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        
        if i != largest:
            self.heap[i] , self.heap[largest] = self.heap[largest] , self.heap[i]
            self.heapify(largest,n)

    def build(self,arr):
        self.heap = arr[:]
        n=len(self.heap)
        for i in range( n // 2 -1 ,-1,-1):
            self.heapify(i,n)

        for i in range(n-1,0,-1):
            self.heap[0] ,self.heap[i] = self.heap[i] ,self.heap[0]
            self.heapify(0,i)
        
    

    

heap = Heap()
heap.build([4,2,4,1,7,33,66,34,23,90])
print(heap.heap)
