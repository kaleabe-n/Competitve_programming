class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        dp = [defaultdict(int) for i in range(len(nums))]  
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1 
        return ans
        