class Solution:
    def countOrders(self, n: int) -> int:
        dp = [[None]*501 for _ in range(501)]
        return helper(n,0,dp)
def helper(pick,deli,dp):
    if pick == 0 and deli == 1:
        return 1
    if dp[pick][deli] != None:
        return dp[pick][deli]
    currCount = 0
    if pick>0:
        currCount += pick * helper(pick-1,deli+1,dp)
    if deli>0:
        currCount += deli * helper(pick,deli-1,dp)
    dp[pick][deli] = currCount % (10**9 + 7)
    return currCount % (10**9 + 7)
