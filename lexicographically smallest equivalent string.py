class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i+ord('a')):chr(i+ord('a'))  for i in range(26)}
        for i in range(len(s1)):
            union(s1[i],s2[i],parent)
        ans = []
        for letter in baseStr:
            ans.append(find(letter,parent))
        
        return "".join(ans)
        
        
def union(x,y,parent):
    rootx = find(x,parent)
    rooty = find(y,parent)
    if rootx==rooty:
        return
    if ord(rootx)<ord(rooty):
        rooty,rootx = rootx,rooty
    parent[rootx] = rooty
    
def find(x,parent):
    if x == parent[x]:
        return x
    temp = find(parent[x],parent)
    return temp
        
