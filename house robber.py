class Solution(object):
    def rob(self, nums):
        dp = [None]*len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if i+2>=len(nums):
                dp[i] = nums[i]
            elif i+3>=len(nums):
                dp[i] = nums[i+2] + nums[i]
            else:
                dp[i] = max(dp[i+2],dp[i+3]) + nums[i]
        return max(dp[0],dp[1]) if len(dp)>1 else dp[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        
