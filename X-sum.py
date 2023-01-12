testCount = int(input())
for _ in range(testCount):
    n,m = input().split()
    n = int(n)
    m = int(m)
    grid = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        grid.append(row)
    sumToLeft = dict.fromkeys(list(range(n+m-1)), 0)
    sumToRight = dict.fromkeys(list(range(n,-m-1,-1)),0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sumToLeft[i+j] += grid[i][j]
            sumToRight[i-j] += grid[i][j]
    maxx = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            curr = sumToLeft[i+j] + sumToRight[i-j]
            curr -= grid[i][j]
            maxx = max(maxx,curr)
    print(maxx)
    
