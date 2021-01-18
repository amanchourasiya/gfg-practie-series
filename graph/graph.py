class Graph:
    def __init__(self, V, directed = False):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.directed = directed

    def add_edge(self, u,v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)
    
    def get_adj(self, v):
        return self.adj[v]
    
        