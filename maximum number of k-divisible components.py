class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = collections.defaultdict(list)
        for l,r in edges:
            tree[l].append(r)
            tree[r].append(l)
        return helper(tree,-1,0,values,k)[1]
        
        
def helper(graph,parent,node,values,k):
    currSum = values[node]
    count = 0
    for ne in graph[node]:
        if ne!=parent:
            summ,c = helper(graph,node,ne,values,k)
            currSum += summ
            count += c
    if currSum%k == 0:
        count += 1
    return currSum,count
    
