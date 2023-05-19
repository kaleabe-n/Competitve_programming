class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nums = set()
        for l,r in edges:
            nums.add(l)
            nums.add(r)
        for i in range(len(edges)):
            parent = {i:i for i in nums}
            visited = set
            for j in range(len(edges)):
                if j == i:
                    continue
                l,r = edges[j]
                rroot = root(r,parent)
                lroot = root(l,parent)
                parent[lroot] = rroot
            s = set()
            for k in nums:
                s.add(root(k,parent))
            if len(s) == 1:
                ans = edges[i]
        return ans
        
        
def root(node,parents):
    if node == parents[node]:
        return node
    currRoot = root(parents[node],parents)
    parents[node] = currRoot
    return currRoot
