class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        counts = collections.defaultdict(int)
        for l,r in trips:
            path = dfs(l,r,graph,set([l]))
            for node in path:
                counts[node]+=1
        ans = helper(0,graph,set([0]),counts,price)
        return int(min(ans))
        
def helper(node,graph,visited,counts,price):
    including = (price[node]*counts[node])/2
    without = price[node]*counts[node]
    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            inc,desc = helper(n,graph,visited,counts,price)
            including+=desc
            without+=min(inc,desc)
    return including,without
        
        
            
def dfs(node,target,graph,visited):
    if node == target:
        return [target]
    if len(visited) == len(graph.keys()):
        return
    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            ret = dfs(n,target,graph,visited)
            if ret is not None:
                ret.append(node)
                return ret
    
