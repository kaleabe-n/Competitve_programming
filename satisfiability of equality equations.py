class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i+ord('a')):chr(i+ord('a')) for i in range(26)}
        for eq in equations:
            if eq[1] == '=':
                union(eq[0],eq[3],parent)
        
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0],parent) == find(eq[3],parent):
                    return False
        return True
        
        
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
        
