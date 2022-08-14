from collections import defaultdict

class Solution(object):
    def numEnclaves(self, grid):
        count = 0
        visited = defaultdict(lambda:False)
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if not visited[tuple([j,i])] and grid[j][i] == 1:
                    ans = dfs([j,i],grid,visited,0)
                    if not ans[0]:
                        count+=ans[1]
        return count
        """
        :type grid: List[List[int]]
        :rtype: int
        """

def dfs(location,grid,visited,count):
    count+=1
    visited[tuple(location)] = True
    connectedToEdge = isAtEdge(location,len(grid[0]),len(grid))
    for neighbour in neighbours(location,len(grid[0]),len(grid)):
        if not visited[tuple(neighbour)] and grid[neighbour[0]][neighbour[1]] == 1:
            ans = dfs(neighbour,grid,visited,count)
            connectedToEdge = connectedToEdge or ans[0]
            count = ans[1]
    return [connectedToEdge,count]

        
def neighbours(location,rowLen,colLen):
    neighbours = []
    if location[0]+1<colLen:
        neighbours.append([location[0]+1,location[1]])
    if location[1]+1<rowLen:
        neighbours.append([location[0],location[1]+1])
    if location[0]-1>=0:
        neighbours.append([location[0]-1,location[1]])
    if location[1]-1>=0:
        neighbours.append([location[0],location[1]-1])
    return neighbours


def isAtEdge(location,rowLen,colLen):
    if not location[0]+1<colLen:
        return True
    if not location[1]+1<rowLen:
        return True
    if not location[0]-1>=0:
        return True
    if not location[1]-1>=0:
        return True
    return False
