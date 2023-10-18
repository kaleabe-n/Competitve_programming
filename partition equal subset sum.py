class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        total = sum(nums)
        return helper(0,nums,0,total,set())
def helper(i,nums,currSum,total,dp):
    if currSum == total/2:
        return True
    if i>=len(nums):
        return 0
    if (i,currSum) in dp:
        return False
    if currSum > total/2:
        return False
    ans1 = helper(i+1,nums,currSum+nums[i],total,dp)
    ans2 = helper(i+1,nums,currSum,total,dp)
    dp.add((i,currSum))
    return ans1 or ans2
