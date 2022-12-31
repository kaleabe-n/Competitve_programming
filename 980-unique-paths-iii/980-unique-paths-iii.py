class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        noOfObs = 0
        for i,row in enumerate(grid):
            for j,item in enumerate(row):
                if item == -1:
                    noOfObs += 1
                if item == 1:
                    start = (i,j)
                    
        total = len(grid) * len(grid[0]) - noOfObs
        stack = [[(start[0],start[1]),set([(start[0],start[1])])]]
        ans = 0
        while stack:
            curr,visited = stack.pop()
            if grid[curr[0]][curr[1]] == 2 and len(visited) == total-1:
                ans+=1
            elif grid[curr[0]][curr[1]] == 2:
                pass
            else:
                for i,j in neighbours(curr,grid):
                    if grid[i][j] != -1 and (i,j) not in visited:
                        newVisited = set([x for x in visited])
                        newVisited.add(curr)
                        stack.append([(i,j),newVisited])
        
                    
        return ans
                    
        
            
        

def neighbours(location,grid):
    n = []
    if location[0]-1 >= 0:
        n.append([location[0]-1,location[1]])
    if location[1]-1 >= 0:
        n.append([location[0],location[1]-1])
    if location[0]+1 < len(grid):
        n.append([location[0]+1,location[1]])
    if location[1]+1 < len(grid[0]):
        n.append([location[0],location[1]+1])
    return n
        