class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(count(0,nums,len(nums)-1),count(1,nums,len(nums)))
        
def count(j,nums,end):
    dp = [0]
    for i in range(j,end):
        num = nums[i]
        if i == j:
            dp.append(num)
            continue
        dp.append(max(dp[-1],dp[-2]+num))
    return dp[-1]
    
