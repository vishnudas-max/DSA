class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2, e):
        if v1 in self.graph and v2 in self.graph:
            temp = [e, v2]
            self.graph[v1].append(temp)

    def printgraph(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(i, '---', j[1], '= ', j[0])

    def removeedge(self, v1, v2):
        if v1 in self.graph:
            for edge in self.graph[v1]:
                if edge[1] == v2:
                    self.graph[v1].remove(edge)
                    break

# Example usage:
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(1, 2, 32)
g.add_edge(1, 3, 44)
g.add_edge(3, 3, 43)  # Adding self-loop for testing
print("Graph after adding edges:")
g.printgraph()

print('\nAfter removing edge (3, 3):')
g.removeedge(3, 3)
g.printgraph()
