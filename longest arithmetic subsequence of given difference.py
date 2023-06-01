class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.defaultdict(int)
        maxx = 0
        for num in arr:
            dp[num] = dp[num-difference]+1
            maxx = max(dp[num],maxx)
        return maxx
        
