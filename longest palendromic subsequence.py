class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
        reverseS = list(reversed(s))
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1] == reverseS[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]
