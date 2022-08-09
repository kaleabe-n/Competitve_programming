from collections import defaultdict

class Solution(object):
    
    def floodFill(self, image, sr, sc, color):
        def find(grid,initial,new,location,visited):
            if grid[location[0]][location[1]] == initial and not visited[tuple(location)]:
                visited[tuple(location)] = True
                grid[location[0]][location[1]] = new
                for i in neighbours(location,grid):
                    find(grid,initial,new,i,visited)
        find(image,image[sr][sc],color,[sr,sc],defaultdict(lambda:False))
        return image
                
        
def neighbours(location,grid):
        neighbours = []
        if location[0]-1>=0:
            neighbours.append([location[0]-1,location[1]])
        if location[1]-1>=0:
            neighbours.append([location[0],location[1]-1])
        if location[0]+1<len(grid):
            neighbours.append([location[0]+1,location[1]])
        if location[1]+1<len(grid[0]):
            neighbours.append([location[0],location[1]+1])
        return neighbours
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
