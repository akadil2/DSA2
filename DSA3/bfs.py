from collections import deque
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_edge(self,src,dest):
        if src not in self.vertices:
            self.vertices[src]=[]
        if dest not in self.vertices:
            self.vertices[dest]=[]
        
        self.vertices[src].append(dest)
        self.vertices[dest].append(src)
    
    def bfs(self,start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                queue.extend(self.vertices[vertex])
        return traversal
    
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

print("BFS Traversal:", g.bfs('A'))

