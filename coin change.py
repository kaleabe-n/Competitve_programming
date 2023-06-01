class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp = collections.defaultdict(lambda :float('inf'))
        for c in coins:
            dp[c] = 1
        for i in range(1,amount+1):
            if i in dp:
                continue
            else:
                for c in coins:
                    if dp[i-c]!=float('inf'):
                        dp[i] = min(dp[i],dp[i-c]+1)
                        
        return dp[amount] if dp[amount]!=float('inf') else -1
            
