class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<=1:
            return n
        arr = [None]*(n+1)
        arr[0] = 0
        arr[1] = 1
        maxx = 1
        for i in range(2,n+1):
            if i%2:
                arr[i] = arr[i//2]+arr[i//2+1]
            else:
                arr[i] = arr[i//2]
            maxx = max(maxx,arr[i])
            
        return maxx
