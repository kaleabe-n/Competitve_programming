class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def isValid(x,y):
            if x<1 or y<1:
                return False
            if y>col or x>row:
                return False
            return True
        directions = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
        prevCells = set()
        parents = {}
        rows = collections.defaultdict(set)
        for day,cell in enumerate(cells):
            x,y = cell
            rows[(x,y)].add(y)
            for i,j in directions:
                if isValid(x+i,y+j) and (x+i,y+j) in prevCells:
                    temp = union((x+i,y+j),(x,y),parents,rows)
                    if temp == col:
                        return day
            prevCells.add((x,y))
                  
        
        
def union(x,y,parent,rows):
    rootx = find(x,parent)
    rooty = find(y,parent)
    if rootx==rooty:
        return len(rows[rootx])
    if rootx < rooty:
        rootx,rooty = rooty,rootx
    parent[rootx] = rooty
    for e in rows[rootx]:
        rows[rooty].add(e)
    return len(rows[rooty])
    
    
def find(x,parent):
    if x not in parent:
        parent[x] = x
    if x == parent[x]:
        return x
    temp = find(parent[x],parent)
    parent[x] = temp
    return temp
