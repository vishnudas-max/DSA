class gr:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v1):
        if v1 not in self.graph:
            self.graph[v1] = []

    def add_edge(self, v1, v2, weight):
        # Add v1 to the graph if not already present
        if v1 not in self.graph:
            self.graph[v1] = []
        # Add v2 to the graph if not already present
        if v2 not in self.graph:
            self.graph[v2] = []
        
        # Add the edge with weight
        self.graph[v1].append((v2, weight))

    def remove_vertex(self, v1):
        # Remove vertex v1 from the graph
        if v1 in self.graph:
            # Remove all edges to this vertex
            for vertex in self.graph:
                self.graph[vertex] = [edge for edge in self.graph[vertex] if edge[0] != v1]
            # Remove the vertex itself
            del self.graph[v1]

    def remove_edge(self, v1, v2):
        # Remove edge from v1 to v2
        if v1 in self.graph:
            self.graph[v1] = [edge for edge in self.graph[v1] if edge[0] != v2]

    def printgr(self):
        for i in self.graph:
            for j, weight in self.graph[i]:
                print(f"{i} ----> {j} (weight: {weight})")

    def bfs(self, sta_vertex):
        visited = []
        queue = []
        queue.append(sta_vertex)

        while queue:
            s = queue.pop(0)
            if s not in visited:
                print(s, end=' ')
                visited.append(s)
                for i, _ in self.graph.get(s, []):
                    queue.append(i)
        print()  # for newline after BFS

    def dfs(self, stat, visited=None):
        if visited is None:
            visited = []

        if stat not in visited:
            visited.append(stat)
            print(stat, end=' ')
            for i, _ in self.graph.get(stat, []):
                self.dfs(i, visited)
        print()  # for newline after DFS

# Example Usage
gr = gr()
gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)

gr.add_edge(1, 2, 10)
gr.add_edge(2, 3, 20)
gr.add_edge(2, 1, 15)
gr.add_edge(3, 3, 25)

print("Graph:")
gr.printgr()

print('BFS starting from vertex 1:')
gr.bfs(1)

print('DFS starting from vertex 1:')
gr.dfs(1)

print("Removing edge (2, 1) and vertex 3:")
gr.remove_edge(2, 1)
gr.remove_vertex(3)

print("Updated Graph:")
gr.printgr()
