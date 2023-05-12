class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        indegree = [0]*n
        for l,r in edges:
            graph[l].append(r)
            indegree[r]+=1
        
        que = collections.deque([[i,[]] for i in range(n) if indegree[i] == 0])
        visited = set([i for i in range(n) if indegree[i]==0])
        ancestors = [set() for i in range(n)]
        while que:
            curr,anc = que.popleft()
            anc = list(anc)+[curr]
            for n in graph[curr]:
                if n not in visited:
                    indegree[n]-=1
                    for a in anc:
                        ancestors[n].add(a)
                    if indegree[n] == 0:
                        que.append([n,ancestors[n]])
                        visited.add(n)
        
        for i,anc in enumerate(ancestors):
            anc = list(anc)
            anc.sort()
            ancestors[i] = anc
        
        return ancestors
            
            
                        
        
