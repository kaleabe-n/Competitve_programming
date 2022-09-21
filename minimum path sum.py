class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = {}
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[i])-1,-1,-1):
                dp[(i,j)] = grid[i][j]
                if i == len(grid)-1 and j == len(grid[i])-1:
                    pass
                elif i == len(grid)-1:
                    dp[(i,j)]+=dp[(i,j+1)]
                elif j == len(grid[i])-1:
                    dp[(i,j)]+=dp[(i+1,j)]
                else:
                    dp[(i,j)]+=min(dp[(i+1,j)],dp[(i,j+1)])
        return dp[(0,0)]
