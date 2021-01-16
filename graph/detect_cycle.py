class Solution:
    def isCyclic(self, V, adj):
        # code here
        stack = []
        #print(V)
        print(adj)
        visited = [False] * V 
        #print()
        stack.append(0)
        #visited[0] = True
        hasCycle = False

        while len(stack) != 0 :
            ele = stack.pop(0)
            print('ele', ele)
            if visited[ele] == True:
                hasCycle = True
                break

            visited[ele] = True
            for i in adj[ele]:
                stack.append(i)
        
        return hasCycle

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