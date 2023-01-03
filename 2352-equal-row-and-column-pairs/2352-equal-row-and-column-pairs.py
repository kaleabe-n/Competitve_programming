from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in grid:
            count[str(row)] += 1
            
        ans = 0
        for j in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])
            ans += count[str(col)]
        return ans
        