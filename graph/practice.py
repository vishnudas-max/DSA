class graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v] = []
    
    def add_edge(self,v1,v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        
    def prit(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(f"{i} ------>{j}")
    
    def bfs(self,star):
        visited = []
        queue = []
        queue.append(star)

        while queue:
            s=queue.pop(0)
            if  not s in visited:
                visited.append(s)
                print(s,end=' ')
            for i in self.graph[s]:
                     queue.append(i)

    def dfs(self,stat,visited = None):
        if visited is None:
            visited = []
        
        if stat not in visited:
            visited.append(stat)
            print(stat,end=' ')
            for i in self.graph[stat]:
                self.dfs(i,visited)


g=graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,2)
g.add_edge(3,2)

g.prit()
g.bfs(1)
g.dfs(1)