class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions =  {1:[[0,1],[0,-1]],
                      2:[[1,0],[-1,0]],
                      3:[[1,0],[0,1]],
                      4:[[0,1],[1,0]],
                      5:[[-1,0],[0,-1]],
                      6:[[0,1],[-1,0]]}  
        
        valid = {1:[[[3,1],[5,1],[1,1]],[[4,2],[6,2],[1,2]]],
                2:[[[2,1],[5,3],[6,1]],[[2,2],[3,2],[4,1]]],
                3:[[[2,1],[5,2],[6,1]],[[1,2],[4,2],[6,2]]],
                4:[[[1,1],[5,1],[3,1]],[[2,1],[6,1],[5,2]]],
                5:[[[2,2],[3,2],[4,1]],[[1,2],[4,2],[6,2]]],
                6:[[[1,1],[3,1],[5,1]],[[2,2],[3,2],[4,1]]]}
        if grid[0][0] == 4:
            nodes = [[0,0,2],[0,0,1]]
        else:
            nodes = [[0,0,1]]
        #gt is the direction through which we got in to the node
        visited = set((0,0))
        while nodes:
            x,y,gt = nodes.pop()
            if x == len(grid)-1 and y == len(grid[0])-1:
                return True
            gt-=1
            di = directions[grid[x][y]][gt]
            currVal = grid[x][y]
            nextNode = x+di[0],y+di[1]
            if not isValid(nextNode[0],nextNode[1],grid):
                continue
            nextVal = grid[nextNode[0]][nextNode[1]]
            if (x+di[0],y+di[1]) in visited:
                continue
            if [nextVal,1] in valid[currVal][gt]:
                nodes.append([x+di[0],y+di[1],1])
                visited.add((x+di[0],y+di[1]))
            elif [nextVal,2] in valid[currVal][gt]:
                nodes.append([x+di[0],y+di[1],2])
                visited.add((x+di[0],y+di[1]))
        return False
def isValid(x,y,grid):
    if x<0 or x>=len(grid):
        return False
    if y<0 or y>=len(grid[0]):
        return False
    return True
