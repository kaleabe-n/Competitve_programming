class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [[sr,sc]]
        visited = [[False for i in range(len(image[0]))]for j in range(len(image))]
        visited[sr][sc] = True
        while stack:
            i,j = stack.pop()
            for x,y in neighbors(i,j,image):
                if not visited[x][y]:
                    stack.append([x,y])
                    visited[x][y] = True
            image[i][j] = color
        return image
        
        
def neighbors(i,j,grid):
    n = []
    if i-1>=0 and grid[i-1][j] == grid[i][j]:
        n.append([i-1,j])
    if j-1>=0 and grid[i][j-1] == grid[i][j]:
        n.append([i,j-1])
    if i+1<len(grid) and grid[i+1][j] == grid[i][j]:
        n.append([i+1,j])
    if j+1<len(grid[0]) and grid[i][j+1] == grid[i][j]:
        n.append([i,j+1])
    return n
    


# from collections import defaultdict

# class Solution(object):
    
#     def floodFill(self, image, sr, sc, color):
#         def find(grid,initial,new,location,visited):
#             if grid[location[0]][location[1]] == initial and not visited[tuple(location)]:
#                 visited[tuple(location)] = True
#                 grid[location[0]][location[1]] = new
#                 for i in neighbours(location,grid):
#                     find(grid,initial,new,i,visited)
#         find(image,image[sr][sc],color,[sr,sc],defaultdict(lambda:False))
#         return image
                
        
# def neighbours(location,grid):
#         neighbours = []
#         if location[0]-1>=0:
#             neighbours.append([location[0]-1,location[1]])
#         if location[1]-1>=0:
#             neighbours.append([location[0],location[1]-1])
#         if location[0]+1<len(grid):
#             neighbours.append([location[0]+1,location[1]])
#         if location[1]+1<len(grid[0]):
#             neighbours.append([location[0],location[1]+1])
#         return neighbours
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type color: int
#         :rtype: List[List[int]]
#         """
        
