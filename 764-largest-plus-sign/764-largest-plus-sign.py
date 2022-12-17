class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dpl = [[float('inf') for i in range(n)]for j in range(n)]
        dpr = [[float('inf') for i in range(n)]for j in range(n)]
        dpu = [[float('inf') for i in range(n)]for j in range(n)]
        dpd = [[float('inf') for i in range(n)]for j in range(n)]
        mines = set([tuple(i) for i in mines])
        arr = [[1 for i in range(n)] for i in range(n)]
        for loc in mines:
            arr[loc[0]][loc[1]] = 0
            dpd[loc[0]][loc[1]] = 0
            dpr[loc[0]][loc[1]] = 0
            dpu[loc[0]][loc[1]] = 0
            dpl[loc[0]][loc[1]] = 0
            if loc[0] > 0:
                count = 1
                for i in range(loc[0]-1,-1,-1):
                    if (i,loc[1]) in mines:
                        break
                    dpd[i][loc[1]] = count
                    count+=1
            if loc[1] > 0:
                count = 1
                for i in range(loc[1]-1,-1,-1):
                    if (loc[0],i) in mines:
                        break
                    dpr[loc[0]][i] = count
                    count+=1
            if loc[0] < n-1:
                count = 1
                for i in range(loc[0]+1,n):
                    if (i,loc[1]) in mines:
                        break
                    dpu[i][loc[1]] = count
                    count+=1
            if loc[1] < n-1:
                count = 1
                for i in range(loc[1]+1,n):
                    if (loc[0],i) in mines:
                        break
                    dpl[loc[0]][i] = count
                    count+=1
        maxx = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    l = min(dpl[i][j],i+1)
                    r = min(dpr[i][j],n-i)
                    u = min(dpu[i][j],j+1)
                    d = min(dpd[i][j],n-j)
                    minn = min(l,r,u,d)
                    maxx = max(maxx,minn)
        return maxx
        
        
