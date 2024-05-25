class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            print('empty')
            return None
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print('empty')
            return None
    
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top:
            self.top =self.top.next
        else:
            print('empty')

    def print_st(self):
        current = self.top
        while current:
            print(current.data,'->',end='')
            current = current.next


    
stack = Stack()
stack.push(4)
stack.push(9)
stack.push(11)
stack.push(29)
stack.push(54)
stack.pop()
stack.print_st()