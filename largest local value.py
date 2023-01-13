class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        largestMatrix = []
        for i in range(len(grid)-2):

            temp = []
            for j in range(len(grid)-2):
                currMax = largest([i,j],grid)
                temp.append(currMax)

            largestMatrix.append(temp)
            
        return largestMatrix
        
def largest(location, grid):
    maxx = 0
    for i in range(3):
        for j in range(3):
            curr = grid[location[0] + i][location[1] + j]
            maxx = max(curr,maxx)
    return maxx
