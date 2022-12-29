class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        oneCols = [0 for i in range(len(grid[0]))]
        oneRows = []
        ans = []
        
        for i in range(len(grid)):
            ones = 0
            for j in range(len(grid[i])):
                ones+=grid[i][j]
                oneCols[j] += grid[i][j]
            oneRows.append(ones)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                diff = 2*oneRows[i] + 2*oneCols[j] - len(grid) - len(grid[i])
                grid[i][j] = diff
        
        
        return grid
            
        
        