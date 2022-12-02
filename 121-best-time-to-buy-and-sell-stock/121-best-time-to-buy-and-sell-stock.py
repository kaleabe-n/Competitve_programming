class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = prices[-1]
        maxProfit = 0
        for i in range(len(prices)-2,-1,-1):
            maxProfit = max(maxx-prices[i],maxProfit)
            if maxx is None or prices[i]>maxx:
                maxx = prices[i]
        return maxProfit if maxProfit>=0 else 0