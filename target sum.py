class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = collections.defaultdict(lambda :[defaultdict(int),defaultdict(int)])
        dp[0][0][-nums[0]] = 1
        dp[0][1][nums[0]] = 1
        pPoss = helper(len(nums)-1,nums,dp,1)
        nPoss = helper(len(nums)-1,nums,dp,0)
        return pPoss[target]+nPoss[target]
        
        
def helper(ind,nums,dp,sign):
    if len(dp[ind][sign])!=0:
        return dp[ind][sign]
    currValues = collections.defaultdict(int)
    pPoss = helper(ind-1,nums,dp,1)
    nPoss = helper(ind-1,nums,dp,0)
    if sign:
        for i in (pPoss):
            currValues[i+nums[ind]]+=pPoss[i]
        for i in (nPoss):
            currValues[i+nums[ind]]+=nPoss[i]
    else:
        for i in (pPoss):
            currValues[i-nums[ind]]+=pPoss[i]
        for i in (nPoss):
            currValues[i-nums[ind]]+=nPoss[i]
    dp[ind][sign] = currValues
    return currValues
    
    
    
