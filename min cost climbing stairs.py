class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [None]*(len(cost)+1)
        dp[len(cost)] = 0
        for i in range(len(cost)-1,-1,-1):
            if i <len(cost)-1:
                dp[i] = cost[i] + min(dp[i+1],dp[i+2])
            else:
                dp[i] = cost[i]+dp[i+1]
        return min(dp[0],dp[1])
        """
        :type cost: List[int]
        :rtype: int
        """
        
