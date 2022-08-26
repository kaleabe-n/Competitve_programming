from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rottenQue = deque()
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == 2:
                    rottenQue.append([j,i])
        minutes = 0
        while rottenQue:
            count = len(rottenQue)
            hasChanged = False
            for i in range(count):
                current = rottenQue.popleft()
                for location in neighbours(current,grid):
                    hasChanged = True
                    grid[location[0]][location[1]] = 2
                    rottenQue.append(location)
            if hasChanged:
                minutes+=1
                hasChanged = False
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == 1:
                    return -1
        return minutes
                        
                    
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
def neighbours(location,grid):
    neighbours = []
    if location[0]-1>=0 and grid[location[0]-1][location[1]] == 1:
        neighbours.append([location[0]-1,location[1]])
    if location[1]-1>=0 and grid[location[0]][location[1]-1] == 1:
        neighbours.append([location[0],location[1]-1])
    if location[0]+1<len(grid) and grid[location[0]+1][location[1]] == 1:
        neighbours.append([location[0]+1,location[1]])
    if location[1]+1<len(grid[0]) and grid[location[0]][location[1]+1] == 1:
        neighbours.append([location[0],location[1]+1])
    return neighbours
