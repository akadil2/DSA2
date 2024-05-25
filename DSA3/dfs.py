
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

    def dfs(self,start):
        visited = set()
        result = []
        def dfs_rec(vertex):
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.vertices[vertex]:
                    dfs_rec(neighbor)
        dfs_rec(start)
        return result
    

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

print(g.dfs('A'))
