class Solution:
    def isCyclic(self, V, adj):
        visited = [False] * V
        recStack = [False] * V

        # Visit depth of every branch separately
        for node in range(V):
            if visited[node] == False:
                if self.isCylicUtil(node, visited, recStack, V,adj) == True:
                    return True
        
        return False

    
    # Traverse depth of every path and check if same node occcurs in stack
    def isCylicUtil(self, v, visited, recStack, V, adj):
        visited[v] = True
        recStack[v] = True

        for neighbour in adj[v]:
            if visited[neighbour] == False:
                if self.isCylicUtil(neighbour, visited, recStack, V, adj) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        
        recStack[v] = False
        return False

def test():
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int, input().strip().split())
            adj[a].append(b)
    
        ob = Solution()
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)


test()  