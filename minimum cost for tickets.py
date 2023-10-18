class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')]*(len(days)+1)
        dp[0] = 0
        one,seven,month = costs
        for i,day in enumerate(days):
            dp[i+1] = min(dp[i+1],dp[i]+one)
            j = 0
            while j<len(days) and days[j]<=days[i]+6:
                j+=1
            dp[j] = min(dp[j],dp[i]+seven)
            j = 0
            while j<len(days) and days[j]<=days[i]+29:
                j+=1
            dp[j] = min(dp[j],dp[i]+month)
        return dp[-1]

