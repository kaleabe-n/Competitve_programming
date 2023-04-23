class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)
        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        ans = [0]*n
        dfs(0,graph,labels,ans,None)
        return ans
        
        
def dfs(node,graph,labels,ans,parent):
    if len(graph[node]) == 1 and graph[node][0] == parent:
        ans[node] = 1
        counts = [0]*26
        counts[ord(labels[node])-ord('a')] = 1
        return counts
    
    count = [0]*26
    count[ord(labels[node])-ord('a')]+=1
    for n in graph[node]:
        if n != parent:
            tempCount = dfs(n,graph,labels,ans,node)
            for i in range(26):
                count[i]+=tempCount[i]
                
    ans[node] = count[ord(labels[node])-ord('a')]
    return count
