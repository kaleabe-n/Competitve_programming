class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        que = collections.deque([[0,0,1]])
        visited = set([(0,0)])
        while que:
            x,y,l = que.popleft()
            if x == len(grid)-1 and y == len(grid[0])-1:
                return l
            for i,j in directions:
                newX = x+i
                newY = y+j
                if isValid(newX,newY,grid) and (newX,newY) not in visited and grid[newX][newY] == 0:
                    visited.add((newX,newY))
                    que.append([newX,newY,l+1])
            
        return -1
            
def isValid(x,y,grid):
    if x<0 or x>=len(grid):
        return False
    if y<0 or y>=len(grid[0]):
        return False
    return True
