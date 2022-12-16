class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxx = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                maxx = max(maxx,grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1]+grid[i][j]+grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1])

        return maxx
