class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = collections.defaultdict(list)
        self.max = 0
        for i,num in enumerate(parent):
            tree[num].append(i)
            
        dfs(0,s,tree,self)
        return self.max
            
        
def dfs(node,s,tree,obj):
    maxes = [0]
    for child in tree[node]:
        curr = dfs(child,s,tree,obj)
        if s[child]!=s[node]:
            maxes.append(curr)
            maxes.sort(reverse = True)
            if len(maxes)>2:
                maxes.pop()
    obj.max = max(obj.max,sum(maxes)+1)
    return maxes[0]+1
    
                
    
