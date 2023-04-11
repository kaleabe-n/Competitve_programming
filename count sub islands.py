class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        nonVisited = set()
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]:
                    nonVisited.add((i,j))
        count = 0
        while nonVisited:
            root = nonVisited.pop()
            stack = [root]
            isSub = True
            while stack:
                x,y = stack.pop()
                isSub = isSub and grid1[x][y]
                for i,j in neighbors(x,y,grid2):
                    if (i,j) in nonVisited:
                        stack.append((i,j))
                        nonVisited.remove((i,j))
                
            if isSub:
                count += 1
    
        return count
        
        
def neighbors(x,y,grid):
    n = []
    if x-1>=0 and grid[x-1][y]:
        n.append((x-1,y))
    if y-1>=0 and grid[x][y-1]:
        n.append([x,y-1])
    if x+1<len(grid) and grid[x+1][y]:
        n.append([x+1,y])
    if y+1<len(grid[0]) and grid[x][y+1]:
        n.append([x,y+1])
    return n
