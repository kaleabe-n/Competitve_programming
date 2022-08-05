class Solution(object):
    def countNegatives(self, grid):
        count = 0
        left = 0
        right = len(grid[0])-1
        start = None
        while right>left:
            if grid[0][(left+right)//2]>=0:
                if grid[0][(left+right)//2+1]<0:
                    count+=len(grid[0])-((left+right)//2+1)
                    start = (left+right)//2
                    break
                else:
                    left = (left+right)//2+1
            else:
                right = (left+right)//2
        if start is None:
            start = left
            count+=len(grid[0])-start if grid[0][start]<0 else len(grid[0])-start-1
        for i in range(1,len(grid)):
            while grid[i][start]<0 and start>=0:
                start-=1
            count+=len(grid[0])-start-1
        return count
                
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
