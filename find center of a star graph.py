class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        maxx = 0
        for i,j in edges:
            graph[i]+=1
            graph[j]+=1
            maxx = max(maxx,i,j,key=lambda x:graph[x])
        
        return  maxx
