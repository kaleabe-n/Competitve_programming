class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == len(grid[0]) == 1:
            return 1
        parent = {}
        count = collections.defaultdict(lambda :1)
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if count[rootx]<count[rooty]:
                rootx,rooty = rooty,rootx
            parent[rooty] = rootx
            if rootx!=rooty:
                count[rootx] += count[rooty]
            return count[rootx]
        def find(x):
            if x in parent:
                if parent[x] == x:
                    return x
                temp = find(parent[x])
                parent[x] = temp
                return temp
            parent[x] = x
            count[x] = 1
            return x
        def neighbours(x,y):
            n = []
            if x-1>=0 and grid[x-1][y]:
                n.append([x-1,y])
            if y-1>=0 and grid[x][y-1]:
                n.append([x,y-1])
            if x+1<len(grid) and grid[x+1][y]:
                n.append([x+1,y])
            if y+1<len(grid[0]) and grid[x][y+1]:
                n.append([x,y+1])
            return n
        empties = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    empties.append([i,j])
                    continue
                for x,y in neighbours(i,j):
                    union((i,j),(x,y))
        maxx = max(count.values()) if len(count.values())>0 else 0
        for i,j in empties:
            roots = set()
            currCount = 1
            for x,y in neighbours(i,j):
                roots.add(find((x,y)))
            for r in roots:
                currCount += count[r]
            maxx = max(maxx,currCount)
        return maxx
        
