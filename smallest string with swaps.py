import heapq

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {i:i for i in range(len(s))}
        counts = collections.defaultdict(int)
        for l,r in pairs:
            union(l,r,parent)
        groups = collections.defaultdict(list)
        for i,letter in enumerate(s):
            heapq.heappush(groups[find(i,parent)],(letter,i))
            
        ans = []    
        for i in range(len(s)):
            ans.append(heapq.heappop(groups[find(i,parent)])[0])
        return "".join(ans)
            
            
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
    parent[x] = temp
    return temp
