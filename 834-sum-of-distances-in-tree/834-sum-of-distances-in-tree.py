class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        if n == 1:
            return [0]
        for i,j in edges:
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)
        count = [1]*n
        visited = set([0])
        self.root = 0
        def dfs(curr,parent,depth):
            o = 1
            for child in graph[curr]:
                if child != parent:
                    o+=dfs(child,curr,depth+1)
                    self.root+=depth+1
            count[curr] = o
            return o
            
        dfs(0,-1,0)
        ans = [0]*n
        def dfs2(curr,parent,ans_p):
            ans[curr] = ans_p
            for child in graph[curr]:
                if child!=parent:
                    dfs2(child,curr,ans_p+n-count[child]-count[child])
        dfs2(0,-1,self.root)
        return ans
            