class MinHeap:
    def __init__(self):
        self.heap = []
    
    def heapify_up(self,idx):
        while idx>0:
            parent = (idx-1)//2
            if self.heap[parent]>self.heap[idx]:
                self.heap[parent],self.heap[idx] = self.heap[idx],self.heap[parent]
                idx = parent
            else:
                break

    def heapify_down(self,idx):
        while True:
            left = 2*idx+1
            right = 2*idx+2
            small = idx

            if left<len(self.heap) and self.heap[left]<self.heap[small]:
                small = left
            if right<len(self.heap) and self.heap[right]<self.heap[small]:
                small = right

            if small!=idx:
                self.heap[idx],self.heap[small]=self.heap[small],self.heap[idx]
                idx = small
            else:
                break
    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
    
    def remove(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root

minheap = MinHeap()
minheap.insert(5)
minheap.insert(2)
minheap.insert(6)
minheap.insert(1)

print(minheap.heap)
minheap.remove()
print(minheap.heap)