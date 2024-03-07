class gr:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,v1):
        if v1 not in self.graph:
            self.graph[v1] = []

    def add_edge(self,v1,v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
    
    def printgr(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(f"{i} ----> {j}")

    def bfs(self,sta_vertex):
        visited = []
        queue =[]
        queue.append(sta_vertex)

        while queue:
            s=queue.pop(0)
            if  s not in visited:
                print(s,end=' ')
                visited.append(s)
                for i in self.graph[s]:
                    queue.append(i)

    def dfs(self,stat,visited=None):
        if visited == None:
            visited = []

        if stat not in visited:
            visited.append(stat)
            print(stat,end=' ')
            for i in self.graph[stat]:
                self.dfs(i,visited)
        


gr=gr()
gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)

gr.add_edge(1,2)
gr.add_edge(2,3)
gr.add_edge(2,1)
gr.add_edge(3,3)

gr.printgr()

print('bfs')
gr.bfs(1)
print('dfs')
gr.dfs(1)