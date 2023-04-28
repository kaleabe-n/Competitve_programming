class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)

        ans = dfs(0,graph,-1,hasApple)
        return ans-2 if ans>0 else 0
        
    
def dfs(node,graph,parent,hasApple):
    dist = 0
    currHasApple = hasApple[node]
    for n in graph[node]:
        if n != parent:
            ans = dfs(n,graph,node,hasApple)
            currHasApple = currHasApple or ans>0
            dist += ans
    if currHasApple:
        dist+=2
            
    return dist
