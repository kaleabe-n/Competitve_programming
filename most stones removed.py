class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {tuple(x):tuple(x) for x in stones}
        for i in parent:
            for j in parent:
                if i[0] == j[0] or i[1] == j[1]:
                    union(i,j,parent)
        
        roots = set()
        for i in parent:
            roots.add(find(i,parent))
        return len(stones)-len(roots)

        
def union(x,y,parent):
    rootx = find(x,parent)
    rooty = find(y,parent)
    if rootx==rooty:
        return
    if rootx<rooty:
        rooty,rootx = rootx,rooty
    parent[rootx] = rooty
    
def find(x,parent):
    if x == parent[x]:
        return x
    temp = find(parent[x],parent)
    return temp
        
