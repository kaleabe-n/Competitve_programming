class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        grid = maze
        que = collections.deque([[entrance[0],entrance[1],0]])
        visited = set([tuple(entrance)])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while que:
            x,y,dist = que.popleft()
            if [x,y]!=entrance and isExit(x,y,grid):
                return dist
            for i,j in directions:
                newX = x+i
                newY = y+j
                if isValid(newX,newY,grid) and (newX,newY) not in visited and grid[newX][newY] == ".":
                    visited.add((newX,newY))
                    que.append([newX,newY,dist+1])
            
        return -1
        
        
def isValid(x,y,grid):
    if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
        return False
    return True

def isExit(x,y,grid):
    if x==0 or y == 0 or x == len(grid)-1 or y == len(grid[0])-1:
        return True
    return False
