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
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')

for vertex, edges in g.vertices.items():
    print(vertex, '->', edges)