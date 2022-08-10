from collections import defaultdict

class Solution(object):
    def maxAreaOfIsland(self, grid):
        visited = defaultdict(lambda:False)
        maxx = 0
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if not visited[tuple([j,i])] and grid[j][i] == 1:
                    maxx = max(maxx,dfs([j,i],visited,0,grid))
        return maxx
        """
        :type grid: List[List[int]]
        :rtype: int
        """
def dfs(location,visited,count,grid):
    count+=1
    visited[tuple(location)] = True
    for i in neighbours(location,len(grid[0]),len(grid)):
        if not visited[tuple(i)] and grid[i[0]][i[1]] == 1:
            visited[tuple(i)] = True
            count = dfs(i,visited,count,grid)
    return count
            
    
    
def neighbours(location,rowLen,colLen):
    neighbours = []
    if location[0]-1>=0:
        neighbours.append([location[0]-1,location[1]])
    if location[0]+1<colLen:
        neighbours.append([location[0]+1,location[1]])
    if location[1]-1>=0:
        neighbours.append([location[0],location[1]-1])
    if location[1]+1<rowLen:
        neighbours.append([location[0],location[1]+1])
    return neighbours
