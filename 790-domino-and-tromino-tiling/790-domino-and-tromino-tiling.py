class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        i = 3
        while i < n:
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % (10**9+7)
            i += 1

        return dp[n - 1]