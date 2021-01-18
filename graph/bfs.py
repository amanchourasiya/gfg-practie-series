import graph

class Solution:
    def bfsOfGraph(self, V, adj):
        bfs = []
        visited = [False] * V

        q = []
        q.append(0)
        visited[0] = True
        while len(q) !=0:
            print('q', q)
            ele = q.pop(0)
            bfs.append(ele)
            for i in adj[ele]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        
        return bfs


def test_bfs():
    a = [(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,2),(1,3),(1,4),(1,5),(1,7),(1,8),(2,3),(2,5),(2,7),(2,8),
         (2,9),(3,4),(3,7),(3,8),(3,9),(4,5),(5,7),(5,9),(6,8),(8,9)]
    
    g = graph.Graph(10, True)
    
    for i,j in a:
        print(g.adj)
        g.add_edge(i,j)
    

    os = Solution()
    print(os.bfsOfGraph(10, g.adj))

test_bfs()         