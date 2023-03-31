class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = [[],[]]
        p = 0
        for num in grid[1]:
            p+=num
            prefix[1].append(p)
        prefix[1].append(0)
        p = 0
        for i in range(len(grid[0])-1,-1,-1):
            p += grid[0][i]
            prefix[0].append(p)
        prefix[0].reverse()
        prefix[0].append(0)
        minn = float('inf')
        for i in range(len(grid[0])):
            curr = max(prefix[0][i+1],prefix[1][i-1])
            if curr<minn:
                minn = curr
            
        return minn
