from collections import defaultdict

n,m = input().split()
n = int(n)
m = int(m)

grid = []
for _ in range(n):
    grid.append(input())

removed = {} 

colSets = [set() for _ in range(m)]
for i in range(n):
    rowSet = set()
    for j in range(m):
        if grid[i][j] not in removed:
            removed[grid[i][j]] = [set(),set()]
        if grid[i][j] in rowSet:
            removed[grid[i][j]][0].add(i)
        if grid[i][j] in colSets[j]:
            removed[grid[i][j]][1].add(j)
        colSets[j].add(grid[i][j])
        rowSet.add(grid[i][j])

decrypted = []
for i in range(n):
    for j in range(m):
        if i in removed[grid[i][j]][0]:
            continue
        if j in removed[grid[i][j]][1]:
            continue
        decrypted.append(grid[i][j])
        
print("".join(decrypted))
        

        
