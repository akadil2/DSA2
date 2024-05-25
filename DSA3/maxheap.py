class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def heapify_up(self,idx):
        while idx>0:
            parent = (idx-1)//2
            if self.heap[parent]<self.heap[idx]:
                self.heap[parent],self.heap[idx]=self.heap[idx],self.heap[parent]
                idx = parent
            else:
                break
    def heapify_down(self,idx):
        while True:
            left = 2*idx+1
            right = 2*idx+2
            largest = idx
            if left<len(self.heap) and self.heap[left]>self.heap[largest]:
                largest = left
            if right<len(self.heap) and self.heap[right]>self.heap[largest]:
                largest = right

            if largest!=idx:
                self.heap[idx],self.heap[largest]= self.heap[largest],self.heap[idx]
                idx = largest
            else:
                break
    
    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

maxheap = MaxHeap()
maxheap.insert(5)
maxheap.insert(6)
maxheap.insert(4)
maxheap.insert(8)

print(maxheap.heap)