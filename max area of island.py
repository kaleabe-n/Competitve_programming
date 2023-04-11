class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nonVisited = set()
        for i,row in enumerate(grid):
            for j,item in enumerate(row):
                if item == 1:
                    nonVisited.add((i,j))
        maxArea = 0
        while nonVisited:
            root = nonVisited.pop()
            stack = [root]
            area = 0
            while stack:
                curr = stack.pop()
                area+=1
                for x,y in neighbors(curr[0],curr[1],grid):
                    if (x,y) in nonVisited:
                        stack.append((x,y))
                        nonVisited.remove((x,y))
            maxArea = max(maxArea,area)
            
        return maxArea
        
        
def neighbors(x,y,grid):
    n = []
    if x-1>=0 and grid[x-1][y]:
        n.append((x-1,y))
    if y-1>=0 and grid[x][y-1]:
        n.append((x,y-1))
    if x+1<len(grid) and grid[x+1][y]:
        n.append((x+1,y))
    if y+1<len(grid[0]) and grid[x][y+1]:
        n.append((x,y+1))
        
    return n



# from collections import defaultdict

# class Solution(object):
#     def maxAreaOfIsland(self, grid):
#         visited = defaultdict(lambda:False)
#         maxx = 0
#         for j in range(len(grid)):
#             for i in range(len(grid[j])):
#                 if not visited[tuple([j,i])] and grid[j][i] == 1:
#                     maxx = max(maxx,dfs([j,i],visited,0,grid))
#         return maxx
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
# def dfs(location,visited,count,grid):
#     count+=1
#     visited[tuple(location)] = True
#     for i in neighbours(location,len(grid[0]),len(grid)):
#         if not visited[tuple(i)] and grid[i[0]][i[1]] == 1:
#             visited[tuple(i)] = True
#             count = dfs(i,visited,count,grid)
#     return count
            
    
    
# def neighbours(location,rowLen,colLen):
#     neighbours = []
#     if location[0]-1>=0:
#         neighbours.append([location[0]-1,location[1]])
#     if location[0]+1<colLen:
#         neighbours.append([location[0]+1,location[1]])
#     if location[1]-1>=0:
#         neighbours.append([location[0],location[1]-1])
#     if location[1]+1<rowLen:
#         neighbours.append([location[0],location[1]+1])
#     return neighbours
