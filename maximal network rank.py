class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for l,r in roads:
            graph[l].add(r)
            graph[r].add(l)
            
        maxNet = 0
        for i in range(0,n):
            for j in range(i+1,n):
                if j in graph[i]:
                    maxNet = max(maxNet,len(graph[i])+len(graph[j])-1)
                else:
                    maxNet = max(maxNet,len(graph[i])+len(graph[j]))
        
        
        return maxNet
