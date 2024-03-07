class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        self.graph[v] = []

    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)

    def printgr(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(f"{i} --> {j}")

    def delete(self, v1, v2):
        if v1 in self.graph:
            for edge in self.graph[v1]:
                if edge == v2:
                    self.graph[v1].remove(edge)
                    break


    def bfs(self, start_node):
        visited = []
        queue = []
        queue.append(start_node)

        while queue:
            s = queue.pop(0)
            if s not in visited:
                print(s, end=' ')
                visited.append(s)
                for neighbour in self.graph[s]:
                    queue.append(neighbour)


    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = []
        if start_node not in visited:
            print(start_node, end=' ')
            visited.append(start_node)
            for neighbour in self.graph[start_node]:
                self.dfs(neighbour, visited)

# Example usage:
gr = Graph()

gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)
gr.add_vertex(4)

gr.add_edge(1, 2)
gr.add_edge(2, 3)
gr.add_edge(3, 3)
gr.delete(3, 3)
print(gr.graph)
print("Graph:")
gr.printgr()

print("\nBFS Traversal from node 1:")
gr.bfs(1)


print("\nDFS Traversal from node 1:")
gr.dfs(1)