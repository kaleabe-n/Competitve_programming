class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if isMagic(i,j,grid):
                    count += 1
        return count


def isMagic(y,x,grid):
    summs = set()
    vertSum = [0,0,0]
    d1Sum = 0
    d2Sum = 0
    nums = set()
    maxx = 0
    minn = float("inf")
    for i in range(3):
        horizontalSum = 0
        for j in range(3):
            horizontalSum += grid[y+i][x+j]
            vertSum[j] += grid[y+i][x+j]
            if i - j == 0:
                d1Sum += grid[y+i][x+j]
            if i + j == 2:
                d2Sum += grid[y+i][x+j]
            nums.add(grid[y+i][x+j])
            maxx = max(maxx,grid[y+i][x+j])
            minn = min(minn,grid[y+i][x+j])
        summs.add(horizontalSum)
    for s in vertSum:
        summs.add(s)
    summs.add(d1Sum)
    summs.add(d2Sum)
    return len(summs) == 1 and len(nums) == 9 and maxx == 9 and minn == 1
