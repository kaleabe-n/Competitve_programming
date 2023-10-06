class Solution:
    def knightDialer(self, n: int) -> int:
        graph = {
            1:[8,6],
            2:[7,9],
            3:[4,8],
            4:[0,9,3],
            5:[],
            6:[7,1,0],
            7:[2,6],
            8:[3,1],
            9:[4,2],
            0:[4,6]
        }
        summ = 0
        dp = {}
        for i in range(10):
            summ += helper(i,n-1,dp,graph)
            summ%=(10**9+7)
        return summ
        
def helper(curr,n,dp,graph):
    if n == 0:
        return 1
    if (curr,n) in dp:
        return dp[(curr,n)]
    currSum = 0
    for nei in graph[curr]:
        currSum += helper(nei,n-1,dp,graph)
    dp[(curr,n)] = currSum
    return currSum
    
    
