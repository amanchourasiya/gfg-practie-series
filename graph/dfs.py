import graph

class Solution:
    def dfsOfGraph(self, V, adj):
        dfs = []
        s = []
        visited = [False] * V
        s.append(0)
        visited[0] = True

        while len(s) !=0:
            ele = s.pop()
            dfs.append(ele)
            adj[ele].reverse()
            for i in adj[ele]:
                if not visited[i]:
                    s.append(i)
                    visited[i] = True
        
        return dfs

def test_dfs():
    a = [(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,2),(1,3),(1,4),(1,5),(1,7),(1,8),(2,3),(2,5),(2,7),(2,8),
         (2,9),(3,4),(3,7),(3,8),(3,9),(4,5),(5,7),(5,9),(6,8),(8,9)]
    
    g = graph.Graph(10, False)

    for i,j in a:
        g.add_edge(i,j)

    #print(g.adj)
    os = Solution()
    print(os.dfsOfGraph(5, [[1,2,3],[0],[0,4], [0], [2]]))

test_dfs()    
        
        