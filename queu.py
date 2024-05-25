class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        self.items.pop(0)
    

q=Queue()
q.enqueue(12)
q.enqueue(24)
q.enqueue(15)
q.enqueue(33)
q.dequeue()
print(q.items)