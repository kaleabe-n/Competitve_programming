class Solution(object):
    def maxProfit(self, prices):
        dp = [None]*len(prices)
        maxx = prices[-1]
        dp[-1] = 0
        maxProfit = 0
        for i in range(len(prices)-2,-1,-1):
            dp[i] = maxx
            maxProfit = max(dp[i]-prices[i],maxProfit)
            if maxx is None or prices[i]>maxx:
                maxx = prices[i]
        return maxProfit if maxProfit>=0 else 0
                
        """
        :type prices: List[int]
        :rtype: int
        """
        
